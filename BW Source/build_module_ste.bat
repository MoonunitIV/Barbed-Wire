:repeat
@C:\Python27\python "C:\Games\MountBlade Warband\Modules\Project X\Project X Source\compile.py"
@C:\Python27\python "C:\Games\MountBlade Warband\Modules\Project X\Project X Source\Skyboxes.py" tag %1 %2 %3 %4 %5 %6 %7 %8 %9
@C:\Python27\python "C:\Games\MountBlade Warband\Modules\Project X\Project X Source\Flora_kinds.py"
@C:\Python27\python "C:\Games\MountBlade Warband\Modules\Project X\Project X Source\Ground_specs.py"
@copy "C:\Games\MountBlade Warband\Modules\Project X\parties.txt" "C:\Games\MountBlade Warband\Modules\Project X\parties.orig.txt" /Y
@copy "C:\Games\MountBlade Warband\Modules\Project X\map_icons.txt" "C:\Games\MountBlade Warband\Modules\Project X\map_icons.orig.txt" /Y
@echo Script processing has ended as of %TIME%
@"C:\Games\MountBlade Warband\Modules\Project X\Map Labels\mapScribbler.exe" -b
@pause
goto:repeat