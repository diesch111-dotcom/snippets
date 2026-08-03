#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_TableWidget_babynames_US2025.py

QTableWidget manages its own internal storage using 
QTableWidgetItem objects, making it ideal for quick 
UI prototypes, small tables, or simpler applications.

source
US Social Security Office

If need be use the Linux Software Manager to install Python3-pyqt6

tested ++ with LinuxMint and SublimeText IDE   vegaseat  02aug2026
'''

from PyQt6.QtWidgets import *
import sys


class BabyNamesTable(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableWidget of 2025 US Baby Names")
        self.resize(350, 250)

        # create table with rows and columns
        rows = 10
        columns = 2
        self.table = QTableWidget(rows, columns, self)
        self.table.setHorizontalHeaderLabels(["Boy", "Girl"])
        # set column 0 to 200px and column 1 to 120px
        self.table.setColumnWidth(0, 120)
        self.table.setColumnWidth(1, 120)

        # baby first names US 2025 in order
        # boy, girl
        data = [
('Liam', 'Olivia'),
('Noah', 'Charlotte'),
('Oliver','Emma'),
('Theodore', 'Amelia'),
('Henry', 'Sophia'),
('James', 'Mia'),
('Elijah', 'Isabella'),
('Mateo', 'Evelyn'),
('William','Sofia'),
('Lucas', 'Eliana')
        ]
        for rank, (boy, girl) in enumerate(data):
            # data fill the appropriate column
            self.table.setItem(rank, 0, QTableWidgetItem(boy))
            self.table.setItem(rank, 1, QTableWidgetItem(girl))

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
    bt = BabyNamesTable()
    bt.show()
    sys.exit(app.exec())
