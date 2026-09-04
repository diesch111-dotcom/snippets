#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" pqt6_absolute_position.py

Absolute position layout using move(x, y) and resize(w, h)

tested with Spyder IDE on LinuxMint  VegasEat 19jul2026
"""

from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame, QLabel


class Demo(QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()

        # set ULcorner x, y and width and height
        x, y, w, h = 500, 200, 300, 100
        self.setGeometry(x, y, w, h)

        label1 = QLabel('hello', self)
        x, y = 10, 10
        label1.move(x, y)
        label1.resize(200, 30)

        text = str(label1.frameSize())
        label1.setText(text)

        # result of label1.framesize()
        # PyQt5.QtCore.QSize(200, 30)  shows w, h
        print('label1:', text)

        label2 = QLabel('world', self)
        label2.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Sunken)
        x, y = 20, 40
        label2.move(x, y)
        label2.resize(300, 30)

        text = str(label2.geometry())
        label2.setText(text)

        # result of label2.geometry()
        # PyQt5.QtCore.QRect(20, 40, 300, 30)  shows x, y, w, h
        print('label2:', text)

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QApplication([])

    demo = Demo()
    demo.show_and_raise()

    app.exec()
