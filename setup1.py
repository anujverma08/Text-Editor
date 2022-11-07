from distutils import version
from cx_Freeze import setup,Executable
import sys
import os
base=None

if sys.platform=='win32':
    base='Win32GUI'

os.environ['TCL_LIBRARY']=r"C:\Program Files (x86)\Python38-32\tcl\tcl8.6"
os.environ['TK_LIBRARY']=r"C:\Program Files (x86)\Python38-32\tcl\tk8.6"

executables =[Executable("TextEditor.py",base=base,icon="notes.png")]

setup(
    name="Text Editor",
    options={"build_exe":{"packages":["tkinter","os","pymysql"],"include_files":["notes.png",'tcl86t.dll','tk86t.dll','icons']}},
    version="1.0",
    author='Anuj',
    description="Tkinter and Sql application",
    executables=executables
    )
