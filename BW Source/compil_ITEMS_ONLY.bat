@echo off
python process_items.py
@del *.pyc
echo.
echo ______________________________
echo.
python unused_items.py
echo Item processing has ended.
echo Press any key to exit. . .
pause>nul