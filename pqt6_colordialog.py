#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_colordialog.py

exploring PyQt's QColorDialog widget

QColor(255, 0, 0).name() would be "#ff0000" for red

QColor.colorNames() gives a list of 148 predefied color names:
['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque',
'black', 'blanchedalmond', 'blue', ...]

tested with Spyder IDE on LinuxMint  VegasEat 20aug2026
'''

# wildcard imports should be okay since the 'Q' prefix limits collision conflicts
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class ColorDialog(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # 
        self.setGeometry(70, 150, 250, 180)
        self.setWindowTitle('ColorDialog')
        # use initial color black (r, g, b) = (0, 0, 0)
        # color.name() would be string #rrggbb = #000000
        color = QColor(0, 0, 0)

        self.button = QPushButton('Dialog', self)
        # position button absolute (x, y)
        self.button.move(20, 20)

        # pyqt5 uses only newer connect syntax
        self.button.clicked.connect(self.showDialog)
        self.setFocus()

        self.widget = QWidget(self)
        # use style sheet to set background color
        # color.name() is a string in "#rrggbb" format
        sf = "QWidget {background-color: %s}"
        self.widget.setStyleSheet(sf % color.name())
        self.widget.setGeometry(130, 22, 100, 100)
        # test red = QColor(255, 0, 0) ...
        print(QColor(255, 0, 0).name())  # #ff0000
        #print(QColor.colorNames())      # list of predefined colors

    def showDialog(self):
        """
        get the color from QColorDialog and
        use it to set a widget's background color
        """
        color = QColorDialog.getColor()
        print(color.name())  # test, shows hexstring
        sf = "QWidget {background-color: %s}"
        self.widget.setStyleSheet(sf % color.name())


app = QApplication([])
cd = ColorDialog()
cd.show()
app.exec()
