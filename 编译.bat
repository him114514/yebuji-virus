@ECHO OFF
pyinstaller -F -w frame_main.py
pyinstaller -F -w frame_B1.py
pyinstaller -F -w frame_B2.py
pyinstaller -F -w frame_B3.py
pause