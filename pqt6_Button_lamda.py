#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_Button_lamda.py

Exploring PyQT's QPushButton button widget
pass each button's argument using lambda

tested with VSCodium IDE on LinuxMint  VegasEat 22aug2026
'''

from PyQt6.QtCore import *
from PyQt5.QtWidgets import *


class MyForm(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(70, 150, 350,120)
        self.setWindowTitle('pass args with lambda')

        # create the widgets
        self.button1 = QPushButton("button1", self)
        self.button2 = QPushButton("button2", self)
        text = '<>'*10
        self.label = QLabel(text, self)

        # use grid layout for the widgets
        grid = QGridLayout(self)
        # addWidget(widget, row, column, rowSpan=1, columnSpan=1)
        grid.addWidget(self.button1, 0, 0)
        grid.addWidget(self.button2, 1, 0)
        grid.addWidget(self.label, 2, 0)
        self.setLayout(grid)

        # connect the buttons to an action function
        # connect(function) only takes a function reference
        # use lambda to pass any arguments to the function
        action1 = lambda: self.onClick("button1 clicked")
        self.button1.clicked.connect(action1)
        action2 = lambda: self.onClick("button2 clicked")
        self.button2.clicked.connect(action2)

    def onClick(self, text):
        self.label.setText('argument is: ' + text)


app =  QApplication([])
form = MyForm()
form.show()
app.exec()