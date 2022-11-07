import sys
from cx_Freeze import setup, Executable
setup( name = "Any Name", version = "3.1",
       options={"build.exe":{"include_files":["tk86t.dll","tk86t.dll","icons","notes"]}},
       description = "Any Description you like",
       executables = [Executable("texteditor.py",base = "Win32GUI")])
