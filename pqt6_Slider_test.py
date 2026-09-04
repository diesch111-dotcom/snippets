#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_Slider_test.py

Explore the PyQt6 QSlider widget
set its orientation, min/max range, initial value and step size
apply optional tick marks

tested using Spyder IDE on LinuxMint  VegasEat 03sep2026
'''

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QLabel, QMainWindow, QSlider, QVBoxLayout, QWidget
)

class MySlider(QWidget):
    def __init__(self):
        super().__init__()
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(100, 100, 400, 100)
        self.setWindowTitle("Move slider...")
        # set the background color
        bisque = "#FFE4C4"
        self.setStyleSheet("QWidget { background-color: bisque }")

        # make slider orientation Horizontal or Vertical
        self.slider = QSlider(Qt.Orientation.Horizontal)

        # set slider min/max range, initial value and step size
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.setSingleStep(1)

        # show visual tick marks (an option)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(10)

        # connect signal to slot/action function
        self.label = QLabel("----")
        self.slider.valueChanged.connect(self.update_label)

        # position widgets
        vbox = QVBoxLayout()
        vbox.addWidget(self.slider)
        vbox.addWidget(self.label)
        self.setLayout(vbox)


    def update_label(self, value):
        '''the action'''
        self.label.setText(f"Slider value: {value}")


app = QApplication([])
mw = MySlider()
mw.show()
app.exec()
