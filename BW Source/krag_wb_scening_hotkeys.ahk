;Made by kraggrim for Mount & Blade Warband. Cheers to Swyter for helping.
/*
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Controls (if users are adjusting they must be changed lower down, this section is just for reference)
;--General--
M = toggle off mouse acceleration when holding G (on by default) 
Ctrl+T makes the Edit Mode window semi-transparent 

;--AI meshing--
spacebar = extrude
F = Fill
C = Connect
U = Subdivide
O = Grow selection
Ctrl+O = Grow selection to max
L = Weld
R = Remove

;--Ground sculpting--
1 = Select Up
2 = Select Down
3 = Select Smooth
4 = Select Level

;--Objects--(only works on already placed objects for now)
Tab = Duplicate selected object and set same scale and position (not rotation)

F = Toggle the Find Props window on/off
P = Toggle the Previously Placed Props menu on/off

Mousewheel up/down = Increase/decrease the value of selected text box

+ = Scale up object by 0.5
Ctrl++ = Scale up object by 0.1
- = Scale down object by 0.5
Ctrl+- = Scale down object by 0.1

Ctrl+1 = Scale object to 1.0
Ctrl+2 = Scale object to 2.0
Ctrl+3 = Scale object to 3.0
Ctrl+4 = Scale object to 4.0
Ctrl+5 = Scale object to 5.0
Ctrl+6 = Scale object to 6.0
Ctrl+7 = Scale object to 7.0
Ctrl+8 = Scale object to 8.0
Ctrl+9 = Scale object to 9.0

Ctrl+L = Hide placed items list (in very heavy scenes can reduce the lag when placing an object)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
*/
DetectHiddenWindows, Off
#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
DllCall("SystemParametersInfo", "UInt", 0x70, "UInt", 0, "UIntP", originalmousespeed, "UInt", 0) ;Save mouse speed on start to reset on exit
Gui, Props_List:New , , Previously Placed Props
Gui, Props_List:Add, Listbox, w260 r13 vPropChoice, %ChoiceVar% ;Red|Green|Blue|Black|White	;example bits
WinGet, IDVar, ID , Edit Mode
Gui, Props_List:+Owner%IDVar% 
WinGetPos , OutX, OutY, OutWidth, OutHeight, Edit Mode
WinGetPos , GOutX, GOutY, , , Edit Mode
PropsListStarted := 0
PropsListShow := 0
PropsListFirst := 0
ChoiceVar := ;barrel|crate|band_a	;favourites not working? pfpfpfpffp
;ControlGet, ChoiceVar, Choice,, ListBox1,  Edit Mode
Gui, Find_Props:New , , Find Props
Gui, Find_Props:Add, Edit, r1 vPropSearchBox w260 -WantReturn, ; was  gPropSearchBoxInput , change to button
Gui,  Find_Props:Add, Button, Default gPropSearchBoxInput w260, Search (1st time for each type is slow)
Gui, Find_Props:Add, Listbox, w260 r13 vPropSearchResults gPropSearchResultsSelect, %PropSearchResultsList% 
Gui, Find_Props:+Owner%IDVar% +ToolWindow -SysMenu  
FindPropsShow := 0
PropsList := 0
ItemsList := 0
FloraList := 0
FPOutWidth := 0
FPOutX := 0
FPOutY := 0
FPOutHeight := 0
PressedF := 0
Gui, Help_Link:New , ,
TransparencyVar := 0
OutputVarTr := 255
StartupRun := 0
;Gui, Help_Link:Add, Link,,  <a href="https://forums.taleworlds.com/index.php?threads/utility-scening-hotkeys-for-warband-ai-meshing-scaling-objects-faster-g-movement-more.463936/">Click here for hotkeys and features list</a>
;Gui, Help_Link:+Owner%IDVar% +ToolWindow -SysMenu -Caption

;WinGet, IDVar2, ID , Find Props
;Gui, Search_Results:New , , Search Results
;Gui, Search_Results:+Owner%IDVar2% 




;;	G-hold Mouse Acceleration	
ToggleGMAcc := 1	;ON by default, switch to 0 for OFF (can be turned off/on with M during Edit Mode)
SpeedMult := 3.3	;amount of accceleration when holding go to move things around
SetTimer GMAcc, 1	;timer frequency in milliseconds, can probably increase this

;;	Update help section with link to controls/thread
;SetTimer HelpWIn, 500	;timer frequency in milliseconds ; unused now
HelpTextSet := 0
;newLine := "`r`n"

SetTimer DynamicTransparency, 250 

OnExit("ExitFunc")	;needs to be high up in the script for some reason

;; Toggle GMAcc
~m::
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
;MsgBox mb active
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
{
ControlGetFocus, FocusVar, Edit Mode
ControlGetFocus, FocusVar2, Find Props
if FocusVar2 = Edit1	;avoid accidental typing switch
	{
	return
	}
else if FocusVar != ListBox1	;so doesn't activate when typing in the prop list
	{
	if ToggleGMAcc = 1
		{
			ToggleGMAcc := 0
			ControlSetText, Button3, Selected Object (Acceleration is OFF), Edit Mode
		}
	else if ToggleGMAcc = 0
		{
			ToggleGMAcc := 1
			ControlSetText, Button3, Selected Object (Acceleration is ON), Edit Mode
		}
	}
}
return

GMAcc:
{
    global ToggleGMAcc
	WinGetActiveTitle, ActiveTitleVar
	If (ToggleGMAcc = 0)
	{
		Return
	}
	else if (ActiveTitleVar = "Mount&Blade Warband")
	{
		KeyIsDown := GetKeyState("g")
		KeyIsDown2 := GetKeyState("Ctrl")
		KeyIsDown3 := GetKeyState("Shift")
		if (KeyIsDown = 1) and (KeyIsDown2 = 0) and (KeyIsDown3 = 0) ;block when control is held
		{
		   Xspeed := 0
		   Yspeed := 0
		   MouseGetPos, xpos, ypos
		   MouseGetPos, xpos2, ypos2
		   if (xposOld != xpos) 
		   {
			  HorizontalDirection := "x is different"
			  xpos2 -= xposOld
			  Xspeed := xpos2
			  Xspeed *= SpeedMult
			  ;Xspeed *= Xspeed
			  ;Xspeed /= 3
		   }
		   	 else 
		   {
			  HorizontalDirection := "x noMove"
		   }
		   
		   if (yposOld != ypos) 
		   {
			  VerticalDirection := "y is different"
			  ypos2 -= yposOld
			  Yspeed := ypos2
			  Yspeed *= SpeedMult
			  ;Yspeed *= Yspeed
			  ;Yspeed /= 3
		   }
		   else 
		   {
			  VerticalDirection := "y noMove"
		   }
		   
		   
		   ;Send, %HorizontalDirection%   and   %VerticalDirection%{Enter}	;testing
		   
		   DllCall("mouse_event", "UInt", 0x0001, "Int", Xspeed, "Int", Yspeed, "UInt", 0, "UPtr", 0)
		   
		   xposOld = %xpos%
		   yposOld = %ypos%
			
		}
		else
		{
			Return
		}
	}
return
}
;;	More GMAcc stuff at bottom (unsure why needs to be there, but stops other stuff working if higher)

/* 
HelpWIn:
{
    If WinActive Mount&Blade Warband
	If WinExist Edit Mode
	WinGetActiveTitle, ActiveTitleVar
	If (ActiveTitleVar = "Edit Mode Help") and (HelpTextSet = 0)
	{
		ControlTextVar := "krag controls and updates are here:" newLine "forums.taleworlds.com/index.php?threads/utility-scening-hotkeys-for-warband-ai-meshing-scaling-objects-faster-g-movement-more.463936/" newLine newLine
		ControlGetText, HelpVar, Edit1, Edit Mode Help
		ControlTextVar .= HelpVar	;append the exisitng after the krag part
		;ControlSetText, Edit1, %ControlTextVar%, Edit Mode Help
		HelpTextSet := 1
	}
	else
	{
		;HelpTextSet := 0
		Return
	}
return
}
 */
 
DynamicTransparency:
{
    #IfWinActive Mount&Blade Warband
	#IfWinExist Edit Mode
	
	global TransparencyVar
	global StartupRun
	global FindPropsShow
	global PropsListShow
	ControlGet OutputVar3, Visible,, Button19,  Edit Mode
	if TransparencyVar = 1
	{
		KeyIsDown := GetKeyState("LButton")
		if KeyIsDown = 0
		{
			;WinGetActiveTitle, ActiveTitleVar
			OutputVarTr := 0
			WinGet, OutputVarTr, Transparent, Edit Mode
			;MouseGetPos, , , WinUnderHwndDT, 
			MouseGetPos, , , HWND, 
			WinGetTitle, ActiveTitleVar, ahk_id %HWND%
			;WinGetText, ActiveTitleVarT, ahk_id %HWND%
			;WinGetTitle, ActiveTitleVarT , ,ActiveTitleVar0,
			;WinGetText, ActiveTitleVar , ,ActiveTitleVar0,
			;Tooltip  %ActiveTitleVar0% . %ActiveTitleVar% . %ActiveTitleVarT%
			;Tooltip  %HWND% . %ActiveTitleVar% . %OutputVarTr%
			If 	(ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") ;(ActiveTitleVar0 = "0xf0764")
			{
				if (OutputVarTr = 100)
				{
					WinSet, Transparent , 200, Edit Mode
					WinSet, Transparent , 200, Find Props
					WinSet, Transparent , 200, Previously Placed Props
				}
			}	
			else if (ActiveTitleVar = "Mount&Blade Warband") 
			{
				if   (OutputVarTr = 200)
				{
					WinSet, Transparent , 100, Edit Mode
					WinSet, Transparent , 100, Find Props
					WinSet, Transparent , 100, Previously Placed Props
				}
			}
		}	
	}
	
	if (StartupRun = 0)
	{
		;ControlGet OutputVar1, Visible,, Button19,  Edit Mode	;add object
		ControlGet OutputVar2, Enabled,, Button39,  Edit Mode	;update weather
		if(OutputVar3 = 1) and (OutputVar2 = 1)	;startup
		{
			;WinSet, ExStyle, ^0x80, , Edit Mode
			WinSet, ExStyle, WS_EX_TOOLWINDOW, Edit Mode
			Control, Disable ,, Button39, Edit Mode
			ControlMove , Button39, , 926, , , Edit Mode
			WinMove , Edit Mode, , , , , 770,
			If (ToggleGMAcc = 1)
			{
				ControlSetText, Button3, Selected Object (Acceleration is ON), Edit Mode
			}
			else If (ToggleGMAcc = 0)
			{
				ControlSetText, Button3, Selected Object (Acceleration is OFF), Edit Mode
			}
			
			If (PropsListShow = 1)
			{
				Gui, Props_List:Show, w%OutWidth% h190 y%GOutY% x%GOutX% NoActivate, Previously Placed Props
				global OutputVarTr
				WinSet, Transparent , %OutputVarTr%, Previously Placed Props
			}
			
		}
		StartupRun := 1
	}	
	else If (OutputVar3 = 1) and not WinExist("Previously Placed Props") and PropsListShow = 1
	{
		;Gui, Props_List:Destroy
		Gui, Props_List:Show, w%OutWidth% h190 y%GOutY% x%GOutX% NoActivate, Previously Placed Props
		global OutputVarTr
		WinSet, Transparent , %OutputVarTr%, Previously Placed Props
		;WinActivate, Mount&Blade Warband
	}
	else If (OutputVar3 = 1) and not WinExist("Find Props") and FindPropsShow = 1
	{
		SpawnFindProps()
	}
return
}



;;	Resize when menu button clicked
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~LButton::
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband") or (ActiveTitleVar = "Edit Mode Help")	;also works for edit mode help
	MouseGetPos, UnderX, UnderY, WinUnderHwnd0, ControlUnder
	;WinGetTitle, WinUnderHwnd , ,WinUnderHwnd0,
	;ControlGetText ControlUnderText, ControlUnder,  Edit Mode
	ControlGet OutputVar1, Visible,, Button19,  Edit Mode	;add object
	ControlGet OutputVar2, Enabled,, Button39,  Edit Mode	;update weather
	
	 if instr(ControlUnder, "Button6") ;or (OutputVar1 = 1)	 ;or (CheckedVar6 = 1)	;objects
	{
		;WinSet, ExStyle, ^0x80, , Edit Mode
		;WinSet, ExStyle, WS_EX_TOOLWINDOW, Edit Mode
		WinSet, Style, -Caption, Edit Mode
		Control, Disable ,, Button39, Edit Mode	;weather button
		ControlMove , Button39, , 926, , , Edit Mode
		WinMove , Edit Mode, , , , , 770,	;275 width brings it in, but looks weird...
		 If (ToggleGMAcc = 1)
		{
			ControlSetText, Button3, Selected Object (Acceleration is ON), Edit Mode
		}
		else If (ToggleGMAcc = 0)
		{
			ControlSetText, Button3, Selected Object (Acceleration is OFF), Edit Mode
		}
		
		If (PropsListShow = 1)
		{
			Gui, Props_List:Show, w%OutWidth% h190 y%GOutY% x%GOutX% NoActivate, Previously Placed Props
			global OutputVarTr
			WinSet, Transparent , %OutputVarTr%, Previously Placed Props
		}

		If (FindPropsShow = 1) ;and not WinExist("Find Props")
		{
			SpawnFindProps()
		}
		
	}
	;/*
	else if instr(ControlUnder, "Button21") ;or instr(ControlUnder, "Button4") or instr(ControlUnder, "Button5") ;or (CheckedVar21 = 1)	;ai mesh
	{
		WinMove , Edit Mode, , , , , 486,	;resizing
		if WinExist("Previously Placed Props") 
		{
			WinGetPos , GOutX, GOutY, , , Previously Placed Props
		}
		Gui, Props_List:Hide
		HideFindProps()
	}
	else if instr(ControlUnder, "Button4") or instr(ControlUnder, "Button5") ;or (CheckedVar4 = 1) or (CheckedVar5 = 1)	;elevate, ground texture 
	{
		WinMove , Edit Mode, , , , , 430,	;resizing
		if WinExist("Previously Placed Props") 
		{
			WinGetPos , GOutX, GOutY, , , Previously Placed Props
		}
		Gui, Props_List:Hide
		HideFindProps()
	}
	else if instr(ControlUnder, "Button38") or instr(ControlUnder, "Button7") ;or (CheckedVar38 = 1) or (CheckedVar7 = 1)  ;weather and ground colour
	{
		Control, Enable ,, Button39, Edit Mode
		ControlMove , Button39, , 752, , , Edit Mode
		WinMove , Edit Mode, , , , , 968,	;default
		if WinExist("Previously Placed Props") 
		{
			WinGetPos , GOutX, GOutY, , , Previously Placed Props
		}
		Gui, Props_List:Hide
		HideFindProps()
	}
	else if instr(ControlUnder, "Button13")	;help start
	{
		Sleep, 330
		HelpTextSet := 1	;reset the help text variable as it needs added every time the help is opened.
		Gui, Help_Link:Add, Text, , Link to extra krag hotkeys-list, controls and features:
		Gui, Help_Link:Add, Edit, w340,  https://forums.taleworlds.com/index.php?threads/utility-scening-hotkeys-for-warband-ai-meshing-scaling-objects-faster-g-movement-more.463936/
		WinGet, IDVar3, ID , Edit Mode ;Help
		Gui, Help_Link:+Owner%IDVar3% +ToolWindow -SysMenu -Caption
		;Gui, Help_Link:+AlwaysOnTop ;+ToolWindow -SysMenu -Caption
		;Gui, Help_Link:+ToolWindow -SysMenu -Caption
		
		WinGetPos , OutXhelp, OutYhelp, OutWidthhelp, OutHeighthelp, Edit Mode Help
		;OutXhelp += OutWidthhelp
		OutYhelp -= 89
		Gui,  Help_Link:Show, w353 h90 x%OutXhelp% y%OutYhelp%, Edit Mode Help
	}
	else if instr(ControlUnder, "Button1") and (HelpTextSet = 1) ;WinExist("Edit Mode Help")	;help exit
	{
		WinClose, Edit Mode Help
		Gui, Help_Link:Hide
		Gui, Help_Link:Destroy
		HelpTextSet := 0	;reset the help text variable as it needs added every time the help is opened.
		
	}
	else if (instr(ControlUnder, "Button1")) and (instr(WinUnderHwnd0, "0x604fc"))	;edit mode exit 
	{
		;MsgBox %ControlUnderText% . %WinUnderHwnd0% . %WinUnderHwnd%	;0x604fc
		;Gui, Help_Link:Destroy
		If WinExist("Previously Placed Props") ;and WinExist("Edit Mode")
		{
		WinGetPos , GOutX, GOutY, , , Previously Placed Props
		Gui, Props_List:Hide
		}

		HideFindProps()
		
		
	}
	/* 
	else if (OutputVar1 = 1) and (OutputVar2 = 1)	;startup
	{
		;WinSet, ExStyle, ^0x80, , Edit Mode
		WinSet, ExStyle, WS_EX_TOOLWINDOW, Edit Mode
		Control, Disable ,, Button39, Edit Mode
		ControlMove , Button39, , 926, , , Edit Mode
		WinMove , Edit Mode, , , , , 770,
		If (ToggleGMAcc = 1)
		{
			ControlSetText, Button3, Selected Object (Acceleration is ON), Edit Mode
		}
		else If (ToggleGMAcc = 0)
		{
			ControlSetText, Button3, Selected Object (Acceleration is OFF), Edit Mode
		}
		
		If (PropsListShow = 1)
		{
			Gui, Props_List:Show, w%OutWidth% h190 y%GOutY% x%GOutX% NoActivate, Previously Placed Props
			global OutputVarTr
			WinSet, Transparent , %OutputVarTr%, Previously Placed Props
		}
	} 
	*/
	else if (instr(ControlUnder, "ComboBox1")) and (OutputVar1 = 1) ;object selection
	{
		SearchTermVar := 
		
		If WinExist("Find Props") ;and WinExist("Edit Mode")
		{
			Sleep, 250
			WinGetPos, FPOutX, FPOutY, FPOutWidth, FPOutHeight, Find Props
			Gui, Find_Props:Destroy
			WinGet, IDVar, ID , Edit Mode
			Gui,  Find_Props:+Owner%IDVar% +ToolWindow -SysMenu ;-Caption	;makes edit mode the "owner"
			Gui, Find_Props:Add, Edit, r1 vPropSearchBox w260 -WantReturn, ; was  gPropSearchBoxInput , change to button
			Gui,  Find_Props:Add, Button, Default gPropSearchBoxInput w260, Search (1st time for each type is slow)
			Gui, Find_Props:Add, Listbox, w260 r13 vPropSearchResults gPropSearchResultsSelect, %PropSearchResultsList% 

			SpawnFindProps()
		}
		
	}
	/* 
	else If (OutputVar1 = 1) and not WinExist("Previously Placed Props") and PropsListShow = 1
	{
		;Gui, Props_List:Destroy
		Gui, Props_List:Show, w%OutWidth% h190 y%GOutY% x%GOutX% NoActivate, Previously Placed Props
		global OutputVarTr
		WinSet, Transparent , %OutputVarTr%, Previously Placed Props
		;WinActivate, Mount&Blade Warband
	}
	
	else If (OutputVar1 = 1) and not WinExist("Find Props") and FindPropsShow = 1
	{
		SpawnFindProps()
	} 
	*/
	
return



;;	Set transparency
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~^t::	;ctrl 
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
{
	;OutputVar = 0
	global OutputVarTr
	global TransparencyVar
	;MsgBox, %OutputVar%
	WinGet, OutputVarTr, Transparent, Edit Mode	
	if (OutputVarTr < 255) ;and (TransparencyVar = 0)	;or (OutputVarTr = 0) ;or (TransparencyVar = 0) ;or (OutputVarTr = OFF) 
	{
		WinSet, Transparent , 255, Edit Mode
		WinSet, Transparent , 255, Find Props
		WinSet, Transparent , 255, Previously Placed Props
		TransparencyVar := 0
	}
	else if (OutputVarTr = 255) or (TransparencyVar = 0) ;or (TransparencyVar = 0) ;or (OutputVarTr = OFF) 
	{
		WinSet, Transparent , 100, Edit Mode
		WinSet, Transparent , 100, Find Props
		WinSet, Transparent , 100, Previously Placed Props
		TransparencyVar := 1
	}
	else
	{
		WinSet, Transparent , 255, Edit Mode
		WinSet, Transparent , 255, Find Props
		WinSet, Transparent , 255, Previously Placed Props
		TransparencyVar := 0
	}
	
	WinGet, OutputVarTr, Transparent, Edit Mode	
}
return



;;;___Objects section___


;;	add to previous prop list
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~RButton::
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
{
	ControlGet OutputVar, Visible,, Button19,  Edit Mode
	ControlGet, CheckedVar, Checked ,, Button19, Edit Mode
	if (OutputVar = 1) and (CheckedVar = 1) 
	{
		PropInList := 0
		global OutputVarTr
		if WinExist("Previously Placed Props")
		{
			WinGetPos , GOutX, GOutY, , , Previously Placed Props
		}
		
		ControlGet, CurChoiceVar, Choice,, ListBox1,  Edit Mode
		;CurChoiceVar .= "||"
		;MsgBox %CurChoiceVar%
		
		ControlGet, CurrentListPPP, List, , ListBox1, Previously Placed Props
		;GuiControlGet, CurrentListPPP, , PropChoice
		;MsgBox %CurrentListPPP%
		;PropInList := 0
		Loop, Parse, CurrentListPPP, `n  ; Rows are delimited by linefeeds (`n).
		{
			;RowNumber := A_Index
			;Loop, Parse, A_LoopField,; %A_Tab%  ; Fields (columns) in each row are delimited by tabs (A_Tab).
			;MsgBox Row #%RowNumber% Col #%A_Index% is %A_LoopField%.
			if (A_LoopField = CurChoiceVar)	 ;(InStr(A_LoopField, SearchTermVar))
			{
				PropInList := 1
			}
			;else
			;{
			;	return
			;}
		}
		;MsgBox %PropInList%
		
		
		If PropInList = 1 ;(InStr(ChoiceVar, CurChoiceVar)) or CurChoiceVar = "Entry Point" or CurChoiceVar = "Passage"
		{
			If (PropsListShow = 1)
			{
				Gui, Props_List:Show, w%OutWidth% h190 y%GOutY% x%GOutX% NoActivate, Previously Placed Props
				global OutputVarTr
				WinSet, Transparent , %OutputVarTr%, Previously Placed Props
			}
			return
		}
		else
		{
			global  PropsListFirst
			;MsgBox %PropsListFirst%
			;CurChoiceVar .= "||"	;moved above
			if PropsListFirst = 1
			{
				ChoiceVar .= "||"	;whole list
			}
			else
			{
				PropsListFirst := 1
			}
			
			ChoiceVar .= CurChoiceVar
			;CurChoiceVar .= ChoiceVar
			;ChoiceVar := CurChoiceVar
			GuiControlGet, OutputVar, Visible , vPropChoice
			if WinExist("Previously Placed Props")  ;(GuiOutputVar = 1)
			{
				WinGetPos , GOutX, GOutY, , , Previously Placed Props
			}
/* 			else 
			{
				Gui, Props_List:Show, , Previously Placed Props
				WinGetPos , GOutX, GOutY, , , Previously Placed Props
			}
 */			Gui, Props_List:Destroy
			;Gui, Props_List:New, -Caption, Previously Placed Props
			WinGet, IDVar, ID , Edit Mode
			Gui, Props_List:+Owner%IDVar% -SysMenu +ToolWindow
			Gui, Props_List:Add, Listbox, w260 r13 vPropChoice gSelectPreviousProp, %ChoiceVar%  ;13 with caption, 15 without
			;GuiControl, Choose, PropChoice, 1
			;GuiControl, ChooseString, PropChoice, CurChoiceVar
			;;Sort?
			If OutputVar = 1
			{
				WinGetPos , OutX, OutY, OutWidth, OutHeight, Edit Mode
				OutY += 768	;was 770
				;OutX += 3
				OutWidth -= 6
				global PropsListStarted
				global PropsListShow
				if PropsListStarted = 0
				{
					Gui, Props_List:Show, w%OutWidth% h190 y%OutY% x%OutX% NoActivate, Previously Placed Props	;was h190 with the Caption, 210 without
					global OutputVarTr
					WinSet, Transparent , %OutputVarTr%, Previously Placed Props
					PropsListStarted := 1
					WinGetPos , GOutX, GOutY, , , Previously Placed Props
					PropsListShow := 1
				}
				else if PropsListShow = 1
				{
					Gui, Props_List:Show, w%OutWidth% h190 y%GOutY% x%GOutX% NoActivate, Previously Placed Props	;was h190 with the Caption, 210 without
					global OutputVarTr
					WinSet, Transparent , %OutputVarTr%, Previously Placed Props
				}
				;Control, Choose, none, ListBox1,  Previously Placed Props	;sets to top of list
				WinActivate, Mount&Blade Warband 
			}
		}


	}
}
return


;;	prop list
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
;~Home::
~p::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
{
	ControlGet OutputVar, Visible,, Button19
	;GuiControlGet, GuiOutputVar, Visible , vPropChoice
	ControlGetFocus, FocusVar, Edit Mode
	ControlGetFocus, FocusVar2, Find Props
	if FocusVar2 = Edit1	;avoid accidental typing switch
	{
	return
	}
	else if FocusVar != ListBox1	;avoid accidental typing switch
	{
		if WinExist("Previously Placed Props")  ;(GuiOutputVar = 1)
		{
			WinGetPos , GOutX, GOutY, , , Previously Placed Props
			Gui, Props_List:Hide
			PropsListShow := 0
			;MsgBox gui1
		}
		else if (OutputVar = 1) and not WinExist Props_List	;(GuiOutputVar = 0)
		{
			PropsListShow := 1
			;MsgBox gui2
			;Gui, Props_List:New , , Props List
			;Gui Props_List:+AlwaysOnTop
			WinGet, IDVar, ID , Edit Mode
			Gui, Props_List:+Owner%IDVar% -SysMenu +ToolWindow ;-Caption	;makes edit mode the "owner"
			;Gui, Add, Text,, Props:
			;Gui, Add, Listbox, r5 vPropChoice, Red|Green|Blue|Black|White	;example bits
			WinGetPos , OutX, OutY, OutWidth, OutHeight, Edit Mode
			OutY += 768	;was 770
			;OutX += 3	;without caption
			OutWidth -= 6
			global OutputVarTr
			global PropsListStarted
			;tooltip %OutputVarTr%
			if PropsListStarted = 0
			{
				PropsListStarted := 1
				OutYMargin := OutY
				OutYMargin += 50
				if OutYMargin >= %A_ScreenHeight%
				{
					;MsgBox %A_ScreenHeight%
					OutY := A_ScreenHeight
					OutY -= 190
				}
				Gui, Props_List:Show, w%OutWidth% h190 y%OutY% x%OutX% NoActivate, Previously Placed Props	;was h190 with the Caption, 210 without
				SetTransparency()
				WinGetPos , GOutX, GOutY, , , Previously Placed Props
			}
			else
			{
				Gui, Props_List:Show, w%OutWidth% h190 y%GOutY% x%GOutX% NoActivate, Previously Placed Props	;was h190 with the Caption, 210 without
				SetTransparency()
				WinGetPos , GOutX, GOutY, , , Previously Placed Props
			}
			;Gui, Props_List:Submit, NoHide
			;MsgBox %PropChoice% 
		}
		;else if IfWinExist Props_List  ;(GuiOutputVar = 1)
		;{
		;	WinGetPos , GOutX, GOutY, , , Previously Placed Props
		;	Gui, Props_List:Hide
		;	PropsListShow := 0
		;	;MsgBox gui3
		;}
	}
}
return

~^e::
WinGet, OutputVarTr, Transparent, Edit Mode
global OutputVarTr
StartupRun := 0
global StartupRun
If WinExist("Previously Placed Props") ;and WinExist("Edit Mode")
{
;WinClose, Edit Mode
WinGetPos , GOutX, GOutY, , , Previously Placed Props
Gui, Props_List:Hide
}

HideFindProps()

return


/*
;; delete all instances of selected object - doesn't work
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
^Delete::
;SendInput {Del}	;doesn't work, why?
WinGet, id, List,,, Program Manager
Loop, %id%
{
    this_id := id%A_Index%
    WinGetClass, this_class%A_Index%, ahk_id %this_id%
    WinGetTitle, this_title%A_Index%, ahk_id %this_id%
}
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband") ;and (1 = 2)
{
	;ControlGetFocus, FocusVar, Edit Mode
	;OutputVar = 0
	ControlGet OutputVar, Visible,, ListBox2
	if (OutputVar = 1) ;and (FocusVar = Button19)
	{
		KeyIsDown := GetKeyState("Ctrl")
		if KeyIsDown = 1
		{
			ControlGet ChoiceVar, Choice,, ListBox2,  Edit Mode
			ControlGet, SelectedItems, List , , ListBox2, Edit Mode
			Loop, Parse, SelectedItems, `n  ; Rows are delimited by linefeeds (`n).
			{
				RowNumber := A_Index
				Loop, Parse, A_LoopField, %A_Tab%  ; Fields (columns) in each row are delimited by tabs (A_Tab).
				;MsgBox Row #%RowNumber% Col #%A_Index% is %A_LoopField%. ;col is nothing
				if ChoiceVar = %A_LoopField%
				{
					;MsgBox Row #%RowNumber% Col #%A_Index% is %A_LoopField%.
					Control, Choose, %RowNumber%, ListBox2,  Edit Mode
					;Control, Delete, %RowNumber% , ListBox2, Edit Mode ;just deletes the visual
					ControlSend, ListBox2, {Del},  Edit Mode	;doesn't work
					SendInput {Delete}	;doesn't work?!
				}
			}
		}
	}
}
return
*/

;; scrollup to increase selected scale/pos textbox values
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~WHeelUp::
~^WHeelUp::
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
{
	ControlGetFocus, FocusVar, Edit Mode
	OutputVar = 0
	ControlGet OutputVar, Visible,, %FocusVar%
	if (OutputVar = 1)	;visible
	{
		ChangeVar := 1
		KeyIsDown := GetKeyState("Ctrl")
		if KeyIsDown = 1
		{
		ChangeVar := 5
		}
		
		if FocusVar = Edit12
		{
		ScaleVar := 1
		ControlGetText, ScaleVar , Edit12,  Edit Mode
		ScaleVar += ChangeVar
		ControlSetText, Edit12, %ScaleVar%, Edit Mode
		}
		else if FocusVar = Edit13
		{
		ScaleVar2 := 1
		ControlGetText, ScaleVar2 , Edit13,  Edit Mode
		ScaleVar2 += ChangeVar
		ControlSetText, Edit13, %ScaleVar2%, Edit Mode
		}
		else if FocusVar = Edit14
		{
		ScaleVar3 := 1
		ControlGetText, ScaleVar3 , Edit14,  Edit Mode
		ScaleVar3 += ChangeVar
		ControlSetText, Edit14, %ScaleVar3%, Edit Mode
		}
		else if FocusVar = Edit1
		{
		PosVar := 1
		ControlGetText, PosVar , Edit1,  Edit Mode
		PosVar += ChangeVar
		ControlSetText, Edit1, %PosVar%, Edit Mode
		}
		else if FocusVar = Edit2
		{
		PosVar2 := 1
		ControlGetText, PosVar2 , Edit2,  Edit Mode
		PosVar2 += ChangeVar
		ControlSetText, Edit2, %PosVar2%, Edit Mode
		}
		else if FocusVar = Edit3
		{
		PosVar3 := 1
		ControlGetText, PosVar3 , Edit3,  Edit Mode
		PosVar3 += ChangeVar
		ControlSetText, Edit3, %PosVar3%, Edit Mode
		}
		else if FocusVar = Edit8	;ground level
		{
		LevelVar := 1
		ControlGetText, LevelVar , Edit8,  Edit Mode
		LevelVar += ChangeVar
		ControlSetText, Edit8, %LevelVar%, Edit Mode
		}
		else if FocusVar = Edit5	;prop variable 1
		{
		VarNoVar := 1
		ControlGetText, VarNoVar , Edit5,  Edit Mode
		VarNoVar += ChangeVar
		ControlSetText, Edit5, %VarNoVar%, Edit Mode
		}
		else if FocusVar = Edit6	;prop variable 1
		{
		VarNoVar := 1
		ControlGetText, VarNoVar , Edit6,  Edit Mode
		VarNoVar += ChangeVar
		ControlSetText, Edit6, %VarNoVar%, Edit Mode
		}
	}
}
return


;; scrolldown to increase selected scale/pos textbox values
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~WHeelDown::
~^WHeelDown::
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
{
	ControlGetFocus, FocusVar, Edit Mode
	OutputVar = 0
	ControlGet OutputVar, Visible,, %FocusVar%
	if (OutputVar = 1)	;visible
	{
		ChangeVar := 1
		KeyIsDown := GetKeyState("Ctrl")
		if KeyIsDown = 1
		{
		ChangeVar := 5
		}
		
		if FocusVar = Edit12
		{
		ScaleVar := 1
		ControlGetText, ScaleVar , Edit12,  Edit Mode
		ScaleVar -= ChangeVar
		ControlSetText, Edit12, %ScaleVar%, Edit Mode
		}
		else if FocusVar = Edit13
		{
		ScaleVar2 := 1
		ControlGetText, ScaleVar2 , Edit13,  Edit Mode
		ScaleVar2 -= ChangeVar
		ControlSetText, Edit13, %ScaleVar2%, Edit Mode
		}
		else if FocusVar = Edit14
		{
		ScaleVar3 := 1
		ControlGetText, ScaleVar3 , Edit14,  Edit Mode
		ScaleVar3 -= ChangeVar
		ControlSetText, Edit14, %ScaleVar3%, Edit Mode
		}
		else if FocusVar = Edit1
		{
		PosVar := 1
		ControlGetText, PosVar , Edit1,  Edit Mode
		PosVar -= ChangeVar
		ControlSetText, Edit1, %PosVar%, Edit Mode
		}
		else if FocusVar = Edit2
		{
		PosVar2 := 1
		ControlGetText, PosVar2 , Edit2,  Edit Mode
		PosVar2 -= ChangeVar
		ControlSetText, Edit2, %PosVar2%, Edit Mode
		}
		else if FocusVar = Edit3
		{
		PosVar3 := 1
		ControlGetText, PosVar3 , Edit3,  Edit Mode
		PosVar3 -= ChangeVar
		ControlSetText, Edit3, %PosVar3%, Edit Mode
		}
		else if FocusVar = Edit8	;ground level
		{
		LevelVar := 1
		ControlGetText, LevelVar , Edit8,  Edit Mode
		LevelVar -= ChangeVar
		ControlSetText, Edit8, %LevelVar%, Edit Mode
		}
		else if FocusVar = Edit5	;prop variable 1
		{
		VarNoVar := 1
		ControlGetText, VarNoVar , Edit5,  Edit Mode
		VarNoVar -= ChangeVar
		ControlSetText, Edit5, %VarNoVar%, Edit Mode
		}
		else if FocusVar = Edit6	;prop variable 1
		{
		VarNoVar := 1
		ControlGetText, VarNoVar , Edit6,  Edit Mode
		VarNoVar -= ChangeVar
		ControlSetText, Edit6, %VarNoVar%, Edit Mode
		}
	}
}
return


;;	Add selected object again
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
;~Enter::
;~NumpadEnter::
~Tab::
OutputVar = 0
;ChoiceVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
	;MsgBox, %this_title2%
	;ControlGet OutputVar, Visible,, ListBox2,  Edit Mode
	ControlGet OutputVar, Visible,, Edit4,  Edit Mode	;listbox2 may be hidden				
	;MsgBox, %OutputVar%.
	if (OutputVar = 1){
		
		;;get name of currenttly selected prop
		;ControlGet ChoiceVar1, Choice,, ListBox2,  Edit Mode	;list of placed items
		ControlGetText ChoiceVar1, Edit4,  Edit Mode	;selected item name shown above the list
		;MsgBox, %ChoiceVar1%
		
		Comboxvar = 0
		If (InStr(ChoiceVar1, "Prop - "))
		{
			Comboxvar = Scene Props
			ChoiceVarCut := SubStr(ChoiceVar1, 12)
		}
		else if (InStr(ChoiceVar1, "Entry Point "))
		{
			Comboxvar = Entry Point
			ChoiceVarCut := "Entry Point"
		}
		else if (InStr(ChoiceVar1, "Item - "))
		{
			Comboxvar = Item Kinds
			ChoiceVarCut := SubStr(ChoiceVar1, 8)
		}
		else if (InStr(ChoiceVar1, "Plant - "))
		{
			Comboxvar = Plants
			ChoiceVarCut := SubStr(ChoiceVar1, 9)
		}
		else if (InStr(ChoiceVar1, "Passage (menu item "))
		{
			Comboxvar = Passage
			ChoiceVarCut := "Passage"
		}
		
		;MsgBox, %Comboxvar%  %ChoiceVarCut%
		
		
		;MsgBox, %ChoiceVarCut%
		
		;;get scale of current prop
		ScaleVar := 1
		ControlGetText, ScaleVar , Edit12,  Edit Mode
		ScaleVar2 := 1
		ControlGetText, ScaleVar2 , Edit13,  Edit Mode
		ScaleVar3 := 1
		ControlGetText, ScaleVar3 , Edit14,  Edit Mode
		
		PosVar := 1
		ControlGetText, PosVar , Edit1,  Edit Mode
		PosVar2 := 1
		ControlGetText, PosVar2 , Edit2,  Edit Mode
		PosVar3 := 1
		ControlGetText, PosVar3 , Edit3,  Edit Mode
		
		ControlGet,  CurrentComboxvar, Choice,, ComboBox1,  Edit Mode
		;MsgBox, %CurrentComboxvar% 
		
		If CurrentComboxvar != %Comboxvar%
		{
			WinActivate, Edit Mode
			Control, ChooseString,  %Comboxvar%, ComboBox1,  Edit Mode
		}
		
		;Control, Choose, Comboxvar, ComboBox1,  Edit Mode
		
		
		;SetControlDelay, -1
		WinActivate, Edit Mode
		Control, ChooseString, %ChoiceVarCut% , ListBox1,  Edit Mode ;works
		;Control, Choose, 2, ListBox1,  Edit Mode ;works
		
		;PostMessage, 0x111, 1075, LBN_SELCHANGE, LBN_SELCHANGE, ListBox1, Edit Mode 	;doesn' work
		;PostMessage, 0x111, 1075, LBN_DBLCLK, LBN_DBLCLK, ListBox1, Edit Mode 			;doesn' work

		;/*
		ControlSetText, Edit12, %ScaleVar%, Edit Mode
		ControlSetText, Edit13, %ScaleVar2%, Edit Mode
		ControlSetText, Edit14, %ScaleVar3%, Edit Mode

		ControlSetText, Edit1, %PosVar%, Edit Mode
		ControlSetText, Edit2, %PosVar2%, Edit Mode
		ControlSetText, Edit3, %PosVar3%, Edit Mode
		;*/
		}
return

;;	copy object position
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~^c::
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
	ControlGet OutputVar, Visible,, ListBox2,  Edit Mode
	ControlGetFocus, FocusVar, Edit Mode
	ControlGet, CheckedVar, Checked ,, Button19, Edit Mode
	if (OutputVar = 1)  and (CheckedVar = 0) and (FocusVar != "Edit12") and (FocusVar != "Edit13") and (FocusVar != "Edit14") and (FocusVar != "Edit1") and (FocusVar != "Edit2") and (FocusVar != "Edit3") and (FocusVar != "Edit5") and (FocusVar != "Edit6")	;avoid accidental typing switch ;and (FocusVar != ListBox1) ;make sure doesn't activate when other textboxes are focused
	{
		SavedXPosVar := 1
		ControlGetText, SavedXPosVar , Edit1,  Edit Mode
		SavedYPosVar := 1
		ControlGetText, SavedYPosVar , Edit2,  Edit Mode
		SavedZPosVar := 1
		ControlGetText, SavedZPosVar , Edit3,  Edit Mode
		;MsgBox positions copied %SavedXPosVar% %SavedYPosVar% %SavedZPosVar% 
	}
return


;;	paste object position
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~^v::
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
	ControlGet OutputVar, Visible,, ListBox2,  Edit Mode
	ControlGet, CheckedVar, Checked ,, Button19, Edit Mode
	ControlGetFocus, FocusVar, Edit Mode
	
	Length := StrLen(SavedYPosVar)	;make sure not blank
	if (OutputVar = 1)  and (CheckedVar = 0) and (Length > 0) and (FocusVar != "Edit12") and (FocusVar != "Edit13") and (FocusVar != "Edit14") and (FocusVar != "Edit1") and (FocusVar != "Edit2") and (FocusVar != "Edit3") and (FocusVar != "Edit5") and (FocusVar != "Edit6")
	{
		ControlSetText, Edit1, %SavedXPosVar%, Edit Mode
		ControlSetText, Edit2, %SavedYPosVar%, Edit Mode
		ControlSetText, Edit3, %SavedZPosVar%, Edit Mode
	}
	;MsgBox %FocusVar%
return


;;	Hide placed items list
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~^l::	;ctrl 
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, ListBox2,  Edit Mode
if (OutputVar = 1){
Control, Hide ,, ListBox2, Edit Mode
Control, Disable,, ListBox2, Edit Mode
}
else
{
Control, Show ,, ListBox2, Edit Mode
Control, Enable,, ListBox2, Edit Mode
}
return





;;	Scale object +0.5
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~=::
~NumpadAdd::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
	;MsgBox, %this_title2%
	ControlGet OutputVar, Visible,, Edit12,  Edit Mode
	;MsgBox, %OutputVar%
	if (OutputVar = 1){

		;ControlGet ScaleVar, Line, N, Edit12,  Edit Mode
		ScaleVar := 0
		ControlGetText, ScaleVar , Edit12,  Edit Mode
		ScaleVar += 0.5
		;MsgBox, %ScaleVar%.

		ScaleVar2 := 0
		ControlGetText, ScaleVar2 , Edit13,  Edit Mode
		ScaleVar2 += 0.5
		ScaleVar3 := 0
		ControlGetText, ScaleVar3 , Edit14,  Edit Mode
		ScaleVar3 += 0.5


		ControlSetText, Edit12, %ScaleVar%, Edit Mode
		ControlSetText, Edit13, %ScaleVar2%, Edit Mode
		ControlSetText, Edit14, %ScaleVar3%, Edit Mode
		}
		
return

;;	Scale object +0.1
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~^=::	;ctrl 
~^NumpadAdd::	;ctrl 
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Edit12,  Edit Mode
if (OutputVar = 1){

ScaleVar := 0
ControlGetText, ScaleVar , Edit12,  Edit Mode
ScaleVar += 0.1
ScaleVar2 := 0
ControlGetText, ScaleVar2 , Edit13,  Edit Mode
ScaleVar2 += 0.1
ScaleVar3 := 0
ControlGetText, ScaleVar3 , Edit14,  Edit Mode
ScaleVar3 += 0.1
ControlSetText, Edit12, %ScaleVar%, Edit Mode
ControlSetText, Edit13, %ScaleVar2%, Edit Mode
ControlSetText, Edit14, %ScaleVar3%, Edit Mode
}
return


;;	Scale object -0.5
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~-::	;minus
~NumpadSub::	;minus
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Edit12,  Edit Mode
if (OutputVar = 1){

ScaleVar := 0
ControlGetText, ScaleVar , Edit12,  Edit Mode
ScaleVar -= 0.5
ScaleVar2 := 0
ControlGetText, ScaleVar2 , Edit13,  Edit Mode
ScaleVar2 -= 0.5
ScaleVar3 := 0
ControlGetText, ScaleVar3 , Edit14,  Edit Mode
ScaleVar3 -= 0.5
ControlSetText, Edit12, %ScaleVar%, Edit Mode
ControlSetText, Edit13, %ScaleVar2%, Edit Mode
ControlSetText, Edit14, %ScaleVar3%, Edit Mode
}
return


;;	Scale object -0.1
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~^-::	;ctrl minus
~^NumpadSub::	;ctrl minus
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Edit12,  Edit Mode
if (OutputVar = 1){

ScaleVar := 0
ControlGetText, ScaleVar , Edit12,  Edit Mode
ScaleVar -= 0.1
ScaleVar2 := 0
ControlGetText, ScaleVar2 , Edit13,  Edit Mode
ScaleVar2 -= 0.1
ScaleVar3 := 0
ControlGetText, ScaleVar3 , Edit14,  Edit Mode
ScaleVar3 -= 0.1
ControlSetText, Edit12, %ScaleVar%, Edit Mode
ControlSetText, Edit13, %ScaleVar2%, Edit Mode
ControlSetText, Edit14, %ScaleVar3%, Edit Mode
}
return


;;	Scale object to 1.0  
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~^1::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Edit12
if (OutputVar = 1){
ScaleVar := 1.0
ControlSetText, Edit12, %ScaleVar%, Edit Mode
ControlSetText, Edit13, %ScaleVar%, Edit Mode
ControlSetText, Edit14, %ScaleVar%, Edit Mode
}
return


;;	Scale object to 2.0  
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~^2::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Edit12
if (OutputVar = 1){
ScaleVar := 2.0
ControlSetText, Edit12, %ScaleVar%, Edit Mode
ControlSetText, Edit13, %ScaleVar%, Edit Mode
ControlSetText, Edit14, %ScaleVar%, Edit Mode
}
return

;;	Scale object to 3.0  
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~^3::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Edit12
if (OutputVar = 1){
ScaleVar := 3.0
ControlSetText, Edit12, %ScaleVar%, Edit Mode
ControlSetText, Edit13, %ScaleVar%, Edit Mode
ControlSetText, Edit14, %ScaleVar%, Edit Mode
}
return

;;	Scale object to 4.0  
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~^4::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Edit12
if (OutputVar = 1){
ScaleVar := 4.0
ControlSetText, Edit12, %ScaleVar%, Edit Mode
ControlSetText, Edit13, %ScaleVar%, Edit Mode
ControlSetText, Edit14, %ScaleVar%, Edit Mode
}
return

;;	Scale object to 5.0  
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~^5::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Edit12
if (OutputVar = 1){
ScaleVar := 5.0
ControlSetText, Edit12, %ScaleVar%, Edit Mode
ControlSetText, Edit13, %ScaleVar%, Edit Mode
ControlSetText, Edit14, %ScaleVar%, Edit Mode
}
return

;;	Scale object to 6.0  
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~^6::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Edit12
if (OutputVar = 1){
ScaleVar := 6.0
ControlSetText, Edit12, %ScaleVar%, Edit Mode
ControlSetText, Edit13, %ScaleVar%, Edit Mode
ControlSetText, Edit14, %ScaleVar%, Edit Mode
}
return

;;	Scale object to 7.0  
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~^7::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Edit12
if (OutputVar = 1){
ScaleVar := 7.0
ControlSetText, Edit12, %ScaleVar%, Edit Mode
ControlSetText, Edit13, %ScaleVar%, Edit Mode
ControlSetText, Edit14, %ScaleVar%, Edit Mode
}
return

;;	Scale object to 8.0  
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~^8::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Edit12
if (OutputVar = 1){
ScaleVar := 8.0
ControlSetText, Edit12, %ScaleVar%, Edit Mode
ControlSetText, Edit13, %ScaleVar%, Edit Mode
ControlSetText, Edit14, %ScaleVar%, Edit Mode
}
return

;;	Scale object to 9.0  
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~^9::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Edit12
if (OutputVar = 1){
ScaleVar := 9.0
ControlSetText, Edit12, %ScaleVar%, Edit Mode
ControlSetText, Edit13, %ScaleVar%, Edit Mode
ControlSetText, Edit14, %ScaleVar%, Edit Mode
}
return






;;;	___AI meshing section___

;;	Extrude    
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
;~q::
~Space::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Extrude
if (OutputVar = 1){
PostMessage, 0x111, 1179, 0, , Edit Mode
}
return


;;	Remove
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~r::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Extrude
if (OutputVar = 1){
PostMessage, 0x111, 1181, 0, , Edit Mode
}
return


;;	Fill & find props
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~f::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
{
	ControlGet OutputVar, Visible,, Button22	;Extrude
	ControlGet OutputVar2, Visible,, Button19
	;GuiControlGet, GuiOutputVar, Visible , vPropChoice
	ControlGetFocus, FocusVar, Edit Mode
	ControlGetFocus, FocusVar2, Find Props
	if (OutputVar = 1)	;extrude visible
	{
		PostMessage, 0x111, 1194, 0, , Edit Mode
		;Gui, Find_Props:Hide	;necessary?
	}
	else if FocusVar = ListBox1	;avoid accidental typing switch
	{
		return
	}
	else if FocusVar2 = Edit1	;avoid accidental typing switch
	{
		return
	}
	else if FocusVar != ListBox1 and FocusVar2 != vPropSearchBox and FocusVar != PropSearchBox and FocusVar2 != Edit1	;avoid accidental typing switch
	{
		global FindPropsShow
		global PressedF
		if WinExist("Find Props")  ;(GuiOutputVar = 1)
		{
			;MsgBox gui1
			;WinGetPos , GOutX, GOutY, , ,  Find Props
			FindPropsShow := 0
			HideFindProps()
		}
		else if (OutputVar2 = 1) ;and not WinExist ("Find Props")	;(GuiOutputVar = 0)
		{
			FindPropsShow := 1
			PressedF := 1
			SpawnFindProps()
			SetTransparency()
		}
	}	
}
;Else          
  ;MsgBox, It's not on top !   
return


;;	Connect
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
;^c::	;the uparrow means it requires ctrl key
~c::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Extrude
if (OutputVar = 1){
PostMessage, 0x111, 1191, 0, , Edit Mode
}
return


;;	Grow Selection
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~o::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Extrude
if (OutputVar = 1){
PostMessage, 0x111, 1190, 0, , Edit Mode
}
return


;;	Select All Connected
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~^o::	;control o
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Extrude
if (OutputVar = 1){
Loop, 1000
{
	PostMessage, 0x111, 1190, 0, , Edit Mode
}
}
return


;;	Subdivide
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~u::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Extrude
if (OutputVar = 1){
PostMessage, 0x111, 1197, 0, , Edit Mode
}
return


;;	Weld
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~l::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Extrude
if (OutputVar = 1){
PostMessage, 0x111, 1196, 0, , Edit Mode
}
return




;;; ___Ground sculpting section___

;;	Up
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~1::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Button8	;Up
if (OutputVar = 1){
ControlGetFocus, FocusVar, Edit Mode	;level box
if FocusVar != Edit8 
{
PostMessage, 0x111, 1140, 0, , Edit Mode
}
}
return
;; Down

#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~2::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Button8	;Up
if (OutputVar = 1){
ControlGetFocus, FocusVar, Edit Mode	;level box
if FocusVar != Edit8 
{PostMessage, 0x111, 1141, 0, , Edit Mode
}
}
return

;; Smooth
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~3::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Button8	;Up
if (OutputVar = 1){
ControlGetFocus, FocusVar, Edit Mode	;level box
if FocusVar != Edit8 
{PostMessage, 0x111, 1142, 0, , Edit Mode
}
}
return

;; Level
#IfWinActive Mount&Blade Warband
#IfWinExist Edit Mode
~4::
OutputVar = 0
CheckEditModeTop()
If (ActiveTitleVar = "Edit Mode") or (ActiveTitleVar = "Previously Placed Props") or (ActiveTitleVar = "Find Props") or (ActiveTitleVar = "Mount&Blade Warband")
ControlGet OutputVar, Visible,, Button8
if (OutputVar = 1){
ControlGetFocus, FocusVar, Edit Mode	;level box
if FocusVar != Edit8 
{PostMessage, 0x111, 1143, 0, , Edit Mode
}
}
return
;;;;;;;;;;;;;;;;;;;;;;


ExitFunc() 
{
  global originalmousespeed
  ;MsgBox %originalmousespeed%
  DllCall("SystemParametersInfo", "UInt", 0x71, "UInt", 0, "UInt", originalmousespeed, "UInt", 0) ;should revert to old mouse speed
}




;;	G-hold Mouse acceleration (GMAcc) stuff, needs to go at the bottom for some reason
~g::
;#IfWinActive Mount&Blade Warband
;#IfWinExist Edit Mode
;WinGet, id, List,,, Program Manager
;Loop, %id%
;{
;    this_id := id%A_Index%
;    WinGetClass, this_class%A_Index%, ahk_id %this_id%
;    WinGetTitle, this_title%A_Index%, ahk_id %this_id%
;}
;;If (InStr(this_title1, "Edit Mode")) or (InStr(this_title2, "Edit Mode")) or (InStr(this_title2, "Previously Placed Props")) or (InStr(this_title2, "Find Props"))
WinGetActiveTitle, ActiveTitleVar
if (ActiveTitleVar = "Mount&Blade Warband")
{
orig := getMouseSpeed()
;ToolTip % orig
setMouseSpeed(1)
;SoundBeep 1500
MouseGetPos, xposOld, yposOld
KeyWait g
setMouseSpeed(orig)
;SoundBeep 1000
}
Return

getMouseSpeed() { ; Get mouse speed
 speed := 0
 DllCall("SystemParametersInfo", "UInt", 0x70, "UInt", 0, "UIntP", speed, "UInt", 0)
 Return speed
}

setMouseSpeed(speed) { ; Set mouse speed
 ; 0x71 (SPI_SETMOUSESPEED), third parameter is the speed (range is 1-20, 10 is default)
 DllCall("SystemParametersInfo", "UInt", 0x71, "UInt", 0, "UInt", speed, "UInt", 0)
}                                                     

CheckEditModeTop() { 
/* 	WinGet, id, List,,, Program Manager	;old method
	Loop, %id%
	{
		this_id := id%A_Index%
		WinGetClass, this_class%A_Index%, ahk_id %this_id%
		WinGetTitle, this_title%A_Index%, ahk_id %this_id%
	}
 */	
global ActiveTitleVar
WinGetActiveTitle, ActiveTitleVar
;MsgBox %ActiveTitleVar%
}                                                     


SelectPreviousProp() { 
	;Gui, Props_List:Submit, NoHide	;why this no work?!
	;ControlGet, CurChoiceVar, Choice,, PropChoice,  Props_List
	GuiControlGet, CurChoiceVar2 , , PropChoice, Value
	;Tooltip %PropChoice% %CurChoiceVar2%
	;Control, ChooseString,  %CurChoiceVar2%, ListBox1,  Edit Mode
	WinActivate, Edit Mode
	ControlFocus , ListBox1,Edit Mode
	;Control, EditPaste, %CurChoiceVar2%, ListBox1,  Edit Mode
	;Send %CurChoiceVar2%,
	SendInput %CurChoiceVar2%
	;ControlSend, ListBox1, %CurChoiceVar2%,  Edit Mode
	;WinActivate, Mount&Blade Warband
}                                                     

PropSearchBoxInput() {
;global SearchTermVar
GuiControlGet, SearchTermVar,, PropSearchBox,

global PropsList
global ItemsList
global FloraList
global FPOutWidth
global FPOutHeight
global FPOutY
global FPOutX

ControlGet,  CurrentComboxvar, Choice,, ComboBox1,  Edit Mode
;ToolTip, %CurrentComboxvar% 

If CurrentComboxvar = Scene Props
{
	;ToolTip, %CurrentComboxvar% 
	CurrentList := PropsList
}
else If CurrentComboxvar = Item Kinds
{
	CurrentList := ItemsList
}
else If CurrentComboxvar = Plants
{
	CurrentList := FloraList
}
/* 
else If CurrentComboxvar = ""
{
	CurrentList := List
}
else If CurrentComboxvar = ""
{
	CurrentList := List
}
 */
Length2 := StrLen(SearchTermVar)	;make sure not blank
	if (Length2 > 0)
	{
		;global PropSearchResults
		global vPropSearchResults
		;global ItemsList ;switch this
		;Sleep, 250

		PropSearchResultsList := 
		;MsgBox %SearchTermVar%
		Length3 := StrLen(CurrentList)
		if (Length3 <= 1)
		{
			;WM_COMMAND bn_clicked 1076 checked
			
			;ControlGet, CheckedVar, Checked ,, Button19, Edit Mode	;just check it either way as sometimes is falsely checked
			;if (CheckedVar = 0) 
			;{
				Control, Check ,, Button19, Edit Mode
				ControlGet, CurrentList, List, , ListBox1, Edit Mode
				;Control, Uncheck ,, Button19, Edit Mode
			;}
			;else
			;{
			;ControlGet, CurrentList, List, , ListBox1, Edit Mode	;HAS TO BE IN ADD OBJECT MODE OR TAKES X10 AS LONG
			;}
			
			;;send it back
			If CurrentComboxvar = Scene Props
			{
				PropsList := CurrentList
			}
			else If CurrentComboxvar = Item Kinds
			{
				ItemsList := CurrentList
			}
			else If CurrentComboxvar = Plants
			{
				FloraList := CurrentList
			}
		}
		
		;ControlGet, SelectedItems, List, Selected, SysListView321, WinTitle
		;ControlGet, CurrentList, List,, ComboBox1, WinTitle
		;Loop, Parse, CurrentList, `n
		;    MsgBox Item number %A_Index% is %A_LoopField%.
			
		Loop, Parse, CurrentList, `n  ; Rows are delimited by linefeeds (`n).
		{
			;RowNumber := A_Index
			;Loop, Parse, A_LoopField,; %A_Tab%  ; Fields (columns) in each row are delimited by tabs (A_Tab).
			;MsgBox Row #%RowNumber% Col #%A_Index% is %A_LoopField%.
			if (InStr(A_LoopField, SearchTermVar))
			{
				PropSearchResultsList .= A_LoopField
				PropSearchResultsList .= "||"
			}
			;else
			;{
			;	return
			;}
		}

						;if (InStr(%this_id%, %SearchTermVar%)
							;PropSearchResultsList .= %this_id%
							;PropSearchResultsList .= "||"

					
		;ControlGet, SelectedItems, List , , PropSearchBox, Find_Props

		;GuiControlGet, SearchTermVar,, PropSearchBox, ;Value
		;Tooltip %SearchTermVar%
		;Gui, Find_Props:Add, Listbox, w260 r10 vPropSearchResults gPropSearchResultsSelect, %SearchTermVar%

		/*	;separate window
		WinGetPos , OutX, OutY, OutWidth, OutHeight, Find Props
		OutWidth -= 6
		Gui, Search_Results:Destroy
		WinGet, IDVar2, ID , Find Props
		Gui, Search_Results:+Owner%IDVar2% +ToolWindow
		Gui, Search_Results:Add, Listbox, w255 r10 vPropSearchResults gPropSearchResultsSelect, %PropSearchResultsList%


		OutY += OutHeight	;was 770, 768

		Gui,  Search_Results:Show, w%OutWidth% h150 y%OutY% x%OutX%, Search Results	;was h190 with the Caption, 210 without
		*/
		
		Length4 := StrLen(PropSearchResultsList)
		if (Length4 <= 1)
		{
			PropSearchResultsList := "No results"
		}
		
		WinGetPos, FPOutX, FPOutY, FPOutWidth, FPOutHeight, Find Props
		Gui, Find_Props:Destroy
		WinGet, IDVar, ID , Edit Mode
		Gui,  Find_Props:+Owner%IDVar% +ToolWindow -SysMenu ;-Caption	;makes edit mode the "owner"
		Gui, Find_Props:Add, Edit, r1 vPropSearchBox w260 -WantReturn, %SearchTermVar%	; was  gPropSearchBoxInput , change to button
		Gui,  Find_Props:Add, Button, Default gPropSearchBoxInput w260, Search ;(1st time for each type is slow)
		Gui, Find_Props:Add, Listbox, w260 r13 vPropSearchResults gPropSearchResultsSelect, %PropSearchResultsList%


		SpawnFindProps()


		WinActivate, Find Props
		ControlFocus , Edit1, Find Props
		;Control, Choose, 1, Edit1, Find Props
		GuiControl, Choose, PropSearchResults, 1
	}
	else if (Length2 <= 0)	;no text
	{
		;Gui, Search_Results:Destroy	;separate window
		WinGetPos, FPOutX, FPOutY, FPOutWidth, FPOutHeight, Find Props
		Gui, Find_Props:Destroy
		WinGet, IDVar, ID , Edit Mode
		Gui,  Find_Props:+Owner%IDVar% +ToolWindow -SysMenu ;-Caption	;makes edit mode the "owner"
		Gui, Find_Props:Add, Edit, r1 vPropSearchBox w260 -WantReturn, ; was  gPropSearchBoxInput , change to button
		Gui,  Find_Props:Add, Button, Default gPropSearchBoxInput w260, Search (1st time for each type is slow)

		SpawnFindProps()
	}
}

PropSearchResultsSelect() { 
	global PropSearchResults
;global vPropSearchResults

	GuiControlGet, PropSearchResultsVar , , PropSearchResults, Value
	;MouseGetPos , OutputVarX, OutputVarY,
	;ControlGetPos , OutXpos, OutYpos, , , ListBox1, Edit Mode
	;MouseMove, OutXpos, OutYpos , 
	WinActivate, Edit Mode
	;ControlClick , ListBox1, Edit Mode
	ControlFocus , ListBox1,Edit Mode
	SendInput %PropSearchResultsVar%
	;MouseMove, OutputVarX, OutputVarY , 
}                                                     

SpawnFindProps() { 
global FPOutWidth
global FPOutHeight
global FPOutY
global FPOutX
global PressedF
;MsgBox %FPOutHeight% in
global OutputVarTr
;WinGet, OutputVarTr, Transparent, Edit Mode
;MsgBox %OutputVarTr%
if FPOutWidth <= 0
{
	WinGet, IDVar, ID , Edit Mode
	Gui,  Find_Props:+Owner%IDVar% +ToolWindow -SysMenu ;+Resize ;-Caption	;makes edit mode the "owner"
	WinGetPos , OutX, OutY, OutWidth, OutHeight, Edit Mode
	OutX += OutWidth
	OutXMargin := OutX
	OutXMargin += OutWidth

	if OutXMargin >= %A_ScreenWidth%
	{
		OutX -= OutWidth
		OutX -= OutWidth
	}
	OutY += 500	;was 770, 768
	OutWidth -= 6
	;Gui,  Find_Props:Show, w%OutWidth% h240 y%OutY% x%OutX% NoActivate, Find Props	;
	Gui,  Find_Props:Show, w284 h240 y%OutY% x%OutX%, Find Props	;
	WinSet, Transparent , %OutputVarTr%, Find Props
}	
else ;if FPOutWidth > 0
{
	;WinGet, IDVar, ID , Edit Mode
	;Gui,  Find_Props:+Owner%IDVar% +ToolWindow -SysMenu
	FPOutWidth -= 6		;why necessary?!
	FPOutHeight -= 29	
	;Gui,  Find_Props:Show, w%FPOutWidth% h%FPOutHeight% y%FPOutY% x%FPOutX% NoActivate, Find Props
	
	if (PressedF = 1)
	{
		Gui,  Find_Props:Show, w284 h240 y%FPOutY% x%FPOutX%, Find Props
		WinSet, Transparent , %OutputVarTr%, Find Props
		PressedF := 0
	}
	else
	{
	Gui,  Find_Props:Show, w284 h240 y%FPOutY% x%FPOutX% NoActivate, Find Props
	WinSet, Transparent , %OutputVarTr%, Find Props
	}
}
}                                                     

HideFindProps() { 
If WinExist("Find Props")
{
	global FPOutWidth
	global FPOutHeight
	global FPOutY
	global FPOutX
	WinGetPos, FPOutX, FPOutY, FPOutWidth, FPOutHeight, Find Props
	;MsgBox %FPOutHeight% out
	Gui, Find_Props:Hide
	
}	
}    

SetTransparency() {
	global TransparencyVar
	if TransparencyVar = 1
	{
		WinSet, Transparent , 100, Edit Mode
		WinSet, Transparent , 100, Find Props
		WinSet, Transparent , 100, Previously Placed Props
	}
	else
	{
		WinSet, Transparent , 255, Edit Mode
		WinSet, Transparent , 255, Find Props
		WinSet, Transparent , 255, Previously Placed Props
	}
	global OutputVarTr
	WinGet, OutputVarTr, Transparent, Edit Mode	
}  

;~^r::Reload  ; Ctrl+R

/* 
~#f6::
WinGet, id, list,,, Program Manager
titles2:=""
Loop, %id%
{
    this_id := id%A_Index%
    WinGetClass, this_class, ahk_id %this_id%
    WinGetTitle, this_title, ahk_id %this_id%
	titles2.=A_Index ": " this_title ";" this_class "`n" 
}
WinGetActiveTitle, ActiveTitleVar
;MsgBox, %ActiveTitleVar%
MsgBox, % titles2
;ControlGet, CheckedVar, Checked ,, Button6, Edit Mode
;MsgBox, % CheckedVar
return  
 */
 
;#IfWinActive Mount&Blade Warband ;
;{
;MButton::g	;remaps
;}



;;by karggrim