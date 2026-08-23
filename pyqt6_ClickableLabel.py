#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pyqt6_ClickableLabel.py

QLabel in PyQt6 doesn't have a built-in clicked signal like QPushButton
so...
subclass QLabel and override its mousePressEvent to make it clickable

tested with VSCodium IDE on LinuxMint  VegasEat 21aug2026
'''

import sys
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout


class ClickableLabel(QLabel):
    # a subclass of QLabel to add click event
    # custom pyqtSignal
    clicked = pyqtSignal()

    def __init__(self, text="", parent=None):
        super().__init__(text, parent)

    # override mousePressEvent to emit the signal
    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(100, 150, 320, 100)

    def initUI(self):
        layout = QVBoxLayout()

        # create the clickable label object
        self.label = ClickableLabel("Click Me!")
        # border-radius: 15px  gives label rounded corners!
        self.label.setStyleSheet(
            "font-size: 18px; padding: 10px; background-color: #e0e0e0; border-radius: 15px;"
        )

        # connect the custom signal to your slot
        self.label.clicked.connect(self.on_label_clicked)

        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setWindowTitle("Clickable QLabel Example")

    def on_label_clicked(self):
        self.label.setText("Label Clicked!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())