#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" pqt6_RadioButton_know.py

Radio buttons are exclusive. only one in a group can be toggled True 
at a time.

tested with Spyder IDE on LinuxMint  VegasEat 19jul2026
"""


from PyQt6.QtWidgets import (
    QApplication, QWidget, QRadioButton, QVBoxLayout, QLabel
)

class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        # set ULcorner x, y and width and height
        x, y, w, h = 500, 200, 300, 100
        self.setGeometry(x, y, w, h)
        self.setWindowTitle("QRadioButton")
        
        vbox = QVBoxLayout()
        
        self.result_label = QLabel("Language Preference")

        # make some Radio Buttons
        self.radio_eng = QRadioButton("English")
        self.radio_can = QRadioButton("Canadian")
        self.radio_esp = QRadioButton("Spanish")
        # make one active...
        self.radio_can.setChecked(True)
        # testing...
        print(self.radio_can.isChecked())  # True

        # use "toggled" for a signal syntax to an action method
        self.radio_eng.toggled.connect(self.update_label)
        self.radio_can.toggled.connect(self.update_label)
        self.radio_esp.toggled.connect(self.update_label)
        
        # position  the widgets in that order...
        vbox.addWidget(self.result_label)
        vbox.addWidget(self.radio_eng)
        vbox.addWidget(self.radio_can)
        vbox.addWidget(self.radio_esp)
        self.setLayout(vbox)

    def update_label(self):
        # self.sender() returns the radio button that triggered the signal
        radio_button = self.sender()
        
        # update if that button turned True
        if radio_button.isChecked():
            self.result_label.setText(f"You know:: {radio_button.text()}")


if __name__ == "__main__":
    app = QApplication([])
    mf = MyForm()
    mf.show()
    app.exec()