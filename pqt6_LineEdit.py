#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_LineEdit.py

Explore PyQT QLineEdit and QLabel connection
update label as you type
QLIneEdit also has Validators and EchoModes
https://doc.qt.io/qt-5/qlineedit.html#EchoMode-enum

Use QLineEdit for the entry of just one line of text
Use QTextEdit for entry and editing of multiple lines

possible docs
https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/index.html#module-PySide6.QtWidgets

tested with VSCodium IDE on LinuxMint  VegasEat 02sep2026
'''

from PyQt6.QtGui import *
# for QWidget, QPushButton, QLabel etc
from PyQt6.QtWidgets import *


class MyForm(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(70, 150, 300, 120)
        self.setWindowTitle("start typing")

        self.edit = QLineEdit(self)
        self.label = QLabel(self)
        # optional style
        self.label.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Sunken)
        # connect line_edit to label
        # update label each time the text has been edited
        # newer connect style used with PyQT 4.5+
        self.edit.textEdited.connect(self.label.setText)
        self.clearButton = QPushButton("Clear")
        self.clearButton.clicked.connect(self.clearText)

        self.label2 = QLabel("Enter an integer:")
        self.edit2 = QLineEdit()
        self.label2r = QLabel()
        # optional style
        self.label2r.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Sunken)
        # now edit2 will only accept integers
        # there is also QDoubleValidator() and QRegExpValidator()
        self.edit2.setValidator(QIntValidator())
        # update label2r each time the text has been edited
        self.edit2.textEdited.connect(self.label2r.setText)

        self.label3 = QLabel("Enter Password:")
        self.edit3 = QLineEdit()
        self.label3r = QLabel()
        # optional style
        self.label3r.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Sunken)
        # now edit3 will echo the password char as *
        # password mode has value 2
        self.edit3.setEchoMode(QLineEdit.EchoMode.Normal)
        # update label3r each time the text has been edited
        self.edit3.textEdited.connect(self.label3r.setText)

        # use grid layout for the widgets
        grid = QGridLayout()
        # addWidget(widget, row, column, rowSpan=1, columnSpan=1)
        grid.addWidget(self.edit, 0, 0, 1, 2)
        grid.addWidget(self.label, 1, 0, 1 , 2)
        grid.addWidget(self.clearButton, 2, 0, 1, 1)
        grid.addWidget(self.label2, 3, 0, 1, 2)
        grid.addWidget(self.edit2, 4, 0, 1, 2)
        grid.addWidget(self.label2r, 5, 0, 1 , 2)
        grid.addWidget(self.label3, 6, 0, 1, 2)
        grid.addWidget(self.edit3, 7, 0, 1, 2)
        grid.addWidget(self.label3r, 8, 0, 1 , 2)
        self.setLayout(grid)

    def clearText(self):
        self.edit.clear()
        self.label.clear()
        print(self.edit.text())  # test


app =  QApplication([])
form = MyForm()
form.show()
app.exec()
