import cx_Freeze
import sys
import os
base=None

if sys.platform=='win32':
    base='Win32GUI'

os.environ['TCL_LIBRARY']=r"C:\Users\pc\AppData\Local\Programs\Python\Python37\tcl\tcl8.6"
os.environ['TK_LIBRARY']=r"C:\Users\pc\AppData\Local\Programs\Python\Python37\tcl\tk8.6"

executables =[cx_Freeze.Executable("TextEditor.py",base=None,icon="notes.ico")]


cx_Freeze.setup(
    name="Text Editor",
    options={"build_exe":{"packages":["tkinter","os",'pymysql','cryptography'],"include_files":["notes.ico",'tcl86t.dll','tk86t.dll','icons','password_file.txt']}},
    version="2.0",
    author="Anuj Verma",
    description="Tkinter and Sql application",
    executables=executables
    )
