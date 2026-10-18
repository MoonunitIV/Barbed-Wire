:repeat
@echo off
fxc /D PS_2_X=ps_2_a /T fx_2_0 /Fo mb.fx mbsrc.fx
pause>nul
goto:repeat