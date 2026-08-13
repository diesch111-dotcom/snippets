#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_TableWidget2.py

QTableWidget manages its own internal storage using 
QTableWidgetItem objects, making it ideal for quick 
UI prototypes, small tables, or simpler applications.

Access Cell Data:
item = table.item(row, col)
text = item.text() if item else ""

Make Cell Read-Only:
item = QTableWidgetItem("Static Text")
item.setFlags(item.flags() ^ Qt.ItemIsEditable)
table.setItem(row, col, item)

Enable Column Sorting:
table.setSortingEnabled(True)

Stretch Columns to Fit Width:
table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

tested with Spyder IDE on LinuxMint  VegasEat 19jul2026
'''

import sys
from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class TableDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableWidget Example")
        self.resize(400, 250)

        # 1. Create table with rows and columns
        self.table = QTableWidget(3, 2, self)
        self.table.setHorizontalHeaderLabels(["Name", "Role"])

        # 2. Populate table with QTableWidgetItems
        data = [
            ("Alice", "Engineer"),
            ("Bob", "Designer"),
            ("Charlie", "Manager")
        ]

        for row, (name, role) in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(role))

        # 3. Connect selection signal
        self.table.cellClicked.connect(self.on_cell_clicked)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

    def on_cell_clicked(self, row, column):
        item = self.table.item(row, column)
        print(f"Clicked cell ({row}, {column}): {item.text()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = TableDemo()
    demo.show()
    sys.exit(app.exec())