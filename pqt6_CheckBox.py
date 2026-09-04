#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_CheckBox.py

Explore the PyQT QCheckBox
shows True when set, otherwise False

tested using Spyder IDE on LinuxMint  VegasEat 03sep2026
'''

from PyQt6.QtCore import Qt
from PyQt5.QtWidgets import  QApplication, QWidget, QCheckBox


class CheckBox(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(320, 200, 300, 120)
        self.setWindowTitle('click on checkbox')

        self.cb = QCheckBox('show status in title', self)
        self.cb.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.cb.move(10, 10)
        # will initially check the box
        self.cb.toggle() 
        self.cb.clicked.connect(self.changeTitle)

    def changeTitle(self, value):
        if self.cb.isChecked():
            self.setWindowTitle('Checkbox set to True')
        else:
            self.setWindowTitle('Checkbox set to False')
        print(self.cb.isChecked())  # test shows True or False


app = QApplication([])
cb = CheckBox()
cb.show()
app.exec()
