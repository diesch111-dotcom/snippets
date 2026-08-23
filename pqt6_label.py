#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_label.py

A detailed look at the QLabel() widget

Can use html code for fancy lettering in a QLabel widget
QLabel in PyQt6 doesn't have a built-in clicked signal like QPushButton
Check pyqt6_ClickableLabel.py for a short subclass

building info...
from PyQt6.QtGui import QColor, QFont

self.

tested with VSCodium IDE on LinuxMint  VegasEat 20aug2026
'''

import sys
import calendar
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class MyLabel(QWidget):
    # inherits QWidget (needed for timing)
    def __init__(self, html_code):
        super().__init__()
        self.html_code = html_code
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(100, 150, 640, 100)
        self.text = 'See if the diuretic works!'
        self.label = QLabel(self.text, self)
        # apply a font
        font = QFont("Times", 40)
        self.label.setFont(font)
        # center text (horizontally and vertically)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # use frame box styling for a cute border
        self.label.setFrameShape(QFrame.Shape.Box)
        self.label.setFrameShadow(QFrame.Shadow.Raised) # Options: Raised, Sunken, Plain
        self.label.setLineWidth(4)
        # set the foreground and background colors of the label
        # the label text is considered foreground 
        fg = "QLabel {color:red}"
        bg = "QLabel {background-color:yellow}"
        # apply with a style sheet
        self.label.setStyleSheet( fg+bg )
        # Set a fixed size (width, height)
        # not needed label expands to fit text
        #self.label.setFixedSize(640, 80)

        self.label2 = QLabel(self.html_code, self)
        # optional style
        #self.label2.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Sunken)

        text = "Nails scratching on a blackboard!"
        self.label3 = QLabel(text, self)
        #  'grey88', '#e0e0e0', (224, 224, 224)
        # border-radius: 15px  gives label rounded corners!
        self.label3.setStyleSheet("""
            font-size: 24px; 
            padding: 10px; 
            background-color: #e0e0e0;
            border-radius: 15px;"""
        )

        month = 6
        year = 1941
        html_cal = calendar.HTMLCalendar()
        html_code_061541 = html_cal.formatmonth(year, month)
        self.label4 = QLabel(html_code_061541, self)

        # use a vertical layout
        vbox = QVBoxLayout()
        # hbox widgets move with window expansion horizontally
        vbox.addStretch(True)
        # add all buttons vertically
        vbox.addWidget(self.label)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.label3)
        vbox.addWidget(self.label4)
        # sets uniform spacing (in pixels) between widgets
        vbox.setSpacing(10) 
        # (left, top, right, bottom) in pixels
        #vbox.setContentsMargins(10, 10, 20, 10)
        self.setLayout(vbox)


html_code = """\
<h1><i>Hello </i>
<font color=red>PyQT</font>
<BR>
<font color=blue>
H<sub>2</sub>O
<BR>
x<sup>3</sup> + y<sup>2</sup> - 15 = 0
</font><h1>
"""

if __name__ == "__main__":
    app = QApplication([])
    win = MyLabel(html_code)
    win.show()
    # start the application's event loop with app.exec()
    # and allow the window corner x click to exit when done
    sys.exit(app.exec())
