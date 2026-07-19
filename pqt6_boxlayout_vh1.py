""" pqt6_boxlayout_vh1.py

Use PyQt QHBoxLayout and QVBoxLayout for a simple box layout of 3 buttons

use the Linux Software Manager to install Python3-pyqt6

tested ++ using the Spyder IDE on Linux OS  dns aka vegaseat  13jul2026
"""

from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtWidgets import QApplication
import sys


class BoxLayout(QWidget):
    def __init__(self, parent=None):
        # Qwidget is self ...
        QWidget.__init__(self, parent)
        self.resize(300, 150)
        self.setWindowTitle('v and h box layout')

        ok = QPushButton("OK")
        cancel = QPushButton("Cancel")
        quit = QPushButton("Quit program")
        quit.clicked.connect(app.closeAllWindows)

        hbox = QHBoxLayout()
        # hbox widgets move with window expansion horizontally
        hbox.addStretch(True)
        # add both buttons horizontally
        hbox.addWidget(ok)
        hbox.addWidget(cancel)
        hbox.addWidget(quit)

        vbox = QVBoxLayout()
        # vbox widgets move with window expansion vertically
        # here it is the widgets in hbox
        vbox.addStretch(True)
        # add hbox sizer to vbox sizer
        vbox.addLayout(hbox)
        # finally set the vbox (is the main sizer)
        self.setLayout(vbox)


app = QApplication(sys.argv)
bx = BoxLayout()
bx.show()

sys.exit(app.exec())
