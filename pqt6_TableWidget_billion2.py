#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_TableWidget_billion2.py

QTableWidget manages its own internal storage using 
QTableWidgetItem objects, making it ideal for quick 
UI prototypes, small tables, or simpler applications.

source
http://en.wikipedia.org/wiki/The_World%27s_Billionaires

here 1 billion is 1_000_000_000 or 1e9

If need be use the Linux Software Manager to install Python3-pyqt6

tested ++ with LinuxMint and SublimeText IDE   vegaseat  19jul2026
'''

from PyQt6.QtWidgets import *
import sys


class BillionairesTable(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableWidget shows 2026 Billionairs")
        self.resize(400, 250)

        # create table with rows and columns
        rows = 10
        columns = 2
        self.table = QTableWidget(rows, columns, self)
        self.table.setHorizontalHeaderLabels(["Name", "Wealth"])
        # set column 0 to 200px and column 1 to 120px
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 120)

        # populate table with QTableWidgetItems
        data = [
('Elon Musk', '$839 billion'),
('Larry Page', '$257 billion'),
('Sergey Brin', '$237 billion'),
('Jeff Bezos', '$224 billion'),
('Mark Zuckerberg', '$222 billion'),
('Larry Ellison', '$190 billion'),
('Bernard Arnault & family', '$171 billion'),
('Jensen Huang', '$154 billion'),
('Warren Buffett', '$149 billion'),
('Amancio Ortega', '$148 billion'),
        ]

        for rank, (name, wealth) in enumerate(data):
            # data fill the appropriate column
            self.table.setItem(rank, 0, QTableWidgetItem(name))
            self.table.setItem(rank, 1, QTableWidgetItem(wealth))

        # connect selection signal
        self.table.cellClicked.connect(self.on_cell_clicked)

        # use box layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

    def on_cell_clicked(self, row, column):
        item = self.table.item(row, column)
        print(f"Clicked cell ({row}, {column}): {item.text()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    bt = BillionairesTable()
    bt.show()
    sys.exit(app.exec())
