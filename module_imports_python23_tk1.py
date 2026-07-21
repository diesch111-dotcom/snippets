''' module_imports_python23_tk1.py
Python 2        Python 3

Dialog          tkinter.dialog
FileDialog      tkinter.FileDialog
ScrolledText    tkinter.scolledtext
SimpleDialog    tkinter.simpledialog
Tix             tkinter.tix
Tkconstants     tkinter.constants
Tkdnd           tkinter.dnd
tkColorChooser  tkinter.colorchooser
tkCommonDialog  tkinter.commondialog
tkFileDialog    tkinter.filedialog
tkFont          tkinter.font
tkMessageBox    tkinter.messagebox
tkSimpleDialog  tkinter.simpledialog
'''

try:
    # Python2
    import Tkinter as tk
    import ttk
    import tkFont as tkf
    import tkColorChooser as cc
    import tkFileDialog as tkfd
    import ScrolledText as tkst
except ImportError:
    # Python3
    import tkinter as tk
    import tkinter.ttk as ttk
    import tkinter.font as tkf
    import tkinter.colorchooser as cc
    import tkinter.filedialog as tkfd
    import tkinter.scrolledtext as tkst
