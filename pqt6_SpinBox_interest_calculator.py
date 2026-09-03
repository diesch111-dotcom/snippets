#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" pqt6_SpinBox_interest_calculator.py

Calculate yearly compound interest
starting with principal, for num years at % rate
Primarily looking at different ways to enter data
click the arrows in the spinbox, can also enter the value directly
The combox limits you to 1 year increments

featuring...
spinbox = QDoubleSpinBox()
spinbox.setValue (float val)
spinbox.setSuffix (" %")
spinbox.setPrefix("$ ")
spinbox.setRannge(int min, max)
years= QComboBox()
grid = QGridLayout()
grid.addWidget(widget, row, column, rowSpan, columnSpan)
setLayout(grid)

tested with IDLE IDE on LinuxMint  VegasEat 25augl2026
"""

# for QDialog, QComboBox, QLabel, QApplication, QDoubleSpinBox etc.
from PyQt6.QtWidgets import *

class InterestCaculator(QDialog):
    """ inherits QDialog """
    def __init__(self, parent=None):
        QDialog.__init__(self)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(100, 150, 350,200)
        self.setWindowTitle("compound Interest (yearly)")

        principalLabel = QLabel("Principal:")
        self.principalSpinBox = QDoubleSpinBox()
        self.principalSpinBox.setRange(1, 10000000)
        self.principalSpinBox.setSingleStep(100)
        self.principalSpinBox.setValue(1000)
        self.principalSpinBox.setPrefix("$ ")
        rateLabel = QLabel("Rate:")
        self.rateSpinBox = QDoubleSpinBox()
        self.rateSpinBox.setRange(0.1, 20.1)
        self.rateSpinBox.setSingleStep(0.1)
        self.rateSpinBox.setValue(4.5)
        self.rateSpinBox.setSuffix(" %")
        yearsLabel = QLabel("Years:")
        self.yearsComboBox = QComboBox()
        self.yearsComboBox.addItem("1 year")
        # list comprehension...
        self.yearsComboBox.addItems([f"{x:d} years"
            for x in range(2, 31)])
        amountLabel = QLabel("Amount (total)")
        self.amountLabel = QLabel()

        grid = QGridLayout()
        # addWidget(widget, row, column, rowSpan, columnSpan)
        # rowSpan, columnSpan default to 1
        grid.addWidget(principalLabel, 0, 0)
        grid.addWidget(self.principalSpinBox, 0, 1)
        grid.addWidget(rateLabel, 1, 0)
        grid.addWidget(self.rateSpinBox, 1, 1)
        grid.addWidget(yearsLabel, 2, 0)
        grid.addWidget(self.yearsComboBox, 2, 1)
        grid.addWidget(amountLabel, 3, 0)
        grid.addWidget(self.amountLabel, 3, 1)
        self.setLayout(grid)

        # newer connect style used
        # eg. self.someButton.clicked.connect(self.onClick)
        self.principalSpinBox.valueChanged.connect(self.update_interest)
        self.rateSpinBox.valueChanged.connect(self.update_interest)
        self.yearsComboBox.currentIndexChanged.connect(self.update_interest)
        self.update_interest()


    def update_interest(self):
        """
        calculates annual compound interest
        """
        principal = self.principalSpinBox.value()
        # annual percentage rate
        rate = self.rateSpinBox.value()
        years = self.yearsComboBox.currentIndex() + 1
        amount = principal * ((1 + (rate / 100.0)) ** years)
        self.amountLabel.setText(f"${amount:0.2f}")


app = QApplication([])
ic = InterestCaculator()
ic.show()
app.exec()
