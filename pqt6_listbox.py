#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_listbox.py

pyqt6 QPushButton and QListWidget (listbox), load and select

tested with Spyder IDE on LinuxMint  VegasEat 20aug2026
'''

# wildcard imports are okay since the 'Q' prefix limits collision conflicts
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class MyListWidget(QWidget):
    def __init__(self, pasta_list):
        QWidget.__init__(self)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(100, 150, 300, 220)
        self.setWindowTitle("Load the listbox first")

        # make pasta_list available for methods
        self.pasta_list = pasta_list

        # use a grid layout for the widgets
        grid = QGridLayout()

        btn_load = QPushButton("Load List")
        # bind the button click to a function reference
        btn_load.clicked.connect(self.on_click)

        self.listbox = QListWidget()
        self.listbox.clicked.connect(self.on_select)

        # addWidget(widget, row, column, rowSpan, columnSpan)
        grid.addWidget(btn_load, 0, 0, 1, 1)
        # listbox spans over 5 rows and 2 columns
        grid.addWidget(self.listbox, 1, 0, 5, 2)
        self.setLayout(grid)

    def on_click(self):
        """the load button has been clicked, load the listbox"""
        self.listbox.addItems(self.pasta_list)
        self.setWindowTitle("Select a pasta ...")

    def on_select(self):
        """an item in the listbox has been clicked/selected"""
        selected_pasta = self.listbox.currentItem().text()
        self.setWindowTitle(selected_pasta)


# data to fill the listbox
# just a few pasta types my mom made
pasta_list = [
'Spaghetti',
'Vermicelli',
'Bucatini',
'Fettuccine',
'Linguine',
'Lasagne',
'Cavatappi',
'Capellini',
'Cannelloni',
'Manicotti',
'Macaroni',
'Penne',
'Rigatoni',
'Fusilli', 
'Rotini', 
'Ziti',
'Farfalle',
'Flaedle',
'Spatzen',
'Maultaschen',
'Tagliatelle',
'Orzo',
'Ditalini', 
'Pastina'
]

app =  QApplication([])
form = MyListWidget(pasta_list)
form.show()
app.exec()

