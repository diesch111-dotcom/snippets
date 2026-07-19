''' pqt6_test_a_widget1.py

A very simple template to test PyQt widgets


If need be use the Linux Software Manager to inststall Python3-pyqt6

tested ++ using the Spyder IDE on Linux OS  dns aka vegaseat  13jul2026
'''

# wildcards okay for testing...
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

app = QApplication([])

# ----- start your widget test code ----

html_code = """\
<h1><i>--- Hello </i>
<font color=red>PyQT! ---</font><h1>
"""
# create the label and insert html code as text
label = QLabel(html_code)
label.show()

# ---- end of widget test code -----

import sys
sys.exit(app.exec())
