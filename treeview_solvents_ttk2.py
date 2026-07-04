#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" treeview_solvents_ttk2.py

Here the ttk.Treeview() widget is configured as a multi-column listbox
with adjustable column width and column-header-click sorting.

It is loaded with a solvent list established way back in my years as
a scientist

docs
https://docs.python.org/3/library/tkinter.ttk.html
https://tkdocs.com/shipman/ttk-Treeview.html


tested using LinuxMint and Spyder IDE  dns(vegaseat)  3jul2026
"""

import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk


class MultiColumnListBox(object):
    """use a ttk.TreeView() as a Multicolumn ListBox"""
    def __init__(self):
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):
        info = """\
click on header to sort by that column
to change width of column drag boundary
        """
        msg = ttk.Label(wraplength="4i", justify="left", anchor="n",
            padding=(10, 2, 10, 6), text=info)
        msg.pack(fill='x')

        container = ttk.Frame()
        container.pack(fill='both', expand=True)

        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=solvent_header, show="headings")
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)

        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in solvent_header:
            self.tree.heading(col, text=col.title(),
                command=lambda co=col: self.sortBy(self.tree, co, 0))
            # adjust the column's width to the header string
            self.tree.column(col, width=tkFont.Font().measure(col.title()))

        for item in solvent_list:
            self.tree.insert('', 'end', values=item)

            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(solvent_header[ix], width=None) < col_w:
                    self.tree.column(solvent_header[ix], width=col_w)

    def isNumeric(self, s):
        """
        test if a string s is numeric
        """
        for c in s:
            if c in "1234567890-.+":
                numeric = True
            else:
                return False
        return numeric

    def changeNumeric(self, data):
        """
        if the data to be sorted is numeric change to float
        """
        new_data = []
        if self.isNumeric(data[0][0]):
            # change child to a float
            for child, col in data:
                new_data.append((float(child), col))
            return new_data
        return data

    def sortBy(self, tree, col, descending):
        """
        sort tree contents when a column header is clicked
        """
        # grab values to sort
        data = [(tree.set(child, col), child) for child in tree.get_children('')]
        # if the data to be sorted is numeric change to float
        data =  self.changeNumeric(data)
        # now sort the data in place
        data.sort(reverse=descending)
        for ix, item in enumerate(data):
            tree.move(item[1], '', ix)
        # switch the heading so that it will sort in the opposite direction
        tree.heading(col,
            command=lambda col=col: self.sortBy(tree, col, int(not descending)))


# the test data ...
solvent_header = ['Solvent Name', '  BP (deg C)', '  MP (deg C)', ' Density (g/ml)']
# don't list the header here
solvent_list = [\
 ['ACETIC ACID', 117.9, 16.7, 1.049],
 ['ACETIC ANHYDRIDE', 140.1, -73.1, 1.087],
 ['ACETONE', 56.3, -94.7, 0.791],
 ['ACETONITRILE', 81.6, -43.8, 0.786],
 ['ANISOLE', 154.2, -37.0, 0.995],
 ['BENZYL ALCOHOL', 205.4, -15.3, 1.045],
 ['BENZYL BENZOATE', 323.5, 19.4, 1.112],
 ['BUTYL ALCOHOL NORMAL', 117.7, -88.6, 0.81],
 ['BUTYL ALCOHOL SEC', 99.6, -114.7, 0.805],
 ['BUTYL ALCOHOL TERTIARY', 82.2, 25.5, 0.786],
 ['CHLOROBENZENE', 131.7, -45.6, 1.111],
 ['CYCLOHEXANE', 80.7, 6.6, 0.779],
 ['CYCLOHEXANOL', 161.1, 25.1, 0.971],
 ['CYCLOHEXANONE', 155.2, -47.0, 0.947],
 ['DICHLOROETHANE 1 2', 83.5, -35.7, 1.246],
 ['DICHLOROMETHANE', 39.8, -95.1, 1.325],
 ['DIETHYL ETHER', 34.5, -116.2, 0.715],
 ['DIMETHYLACETAMIDE', 166.1, -20.0, 0.937],
 ['DIMETHYLFORMAMIDE', 153.3, -60.4, 0.944],
 ['DIMETHYLSULFOXIDE', 189.4, 18.5, 1.102],
 ['DIOXANE 1 4', 101.3, 11.8, 1.034],
 ['DIPHENYL ETHER', 258.3, 26.9, 1.066],
 ['ETHYL ACETATE', 77.1, -83.9, 0.902],
 ['ETHYL ALCOHOL', 78.3, -114.1, 0.789],
 ['ETHYL DIGLYME', 188.2, -45.0, 0.906],
 ['ETHYLENE CARBONATE', 248.3, 36.4, 1.321],
 ['ETHYLENE GLYCOL', 197.3, -13.2, 1.114],
 ['FORMIC ACID', 100.6, 8.3, 1.22],
 ['HEPTANE', 98.4, -90.6, 0.684],
 ['HEXAMETHYL PHOSPHORAMIDE', 233.2, 7.2, 1.027],
 ['HEXANE', 68.7, -95.3, 0.659],
 ['ISO OCTANE', 99.2, -107.4, 0.692],
 ['ISOPROPYL ACETATE', 88.6, -73.4, 0.872],
 ['ISOPROPYL ALCOHOL', 82.3, -88.0, 0.785],
 ['METHYL ALCOHOL', 64.7, -97.7, 0.791],
 ['METHYL ETHYLKETONE', 79.6, -86.7, 0.805],
 ['METHYL ISOBUTYL KETONE', 116.5, -84.0, 0.798],
 ['METHYL T-BUTYL ETHER', 55.5, -10.0, 0.74],
 ['METHYLPYRROLIDINONE N', 203.2, -23.5, 1.027],
 ['MORPHOLINE', 128.9, -3.1, 1.0],
 ['NITROBENZENE', 210.8, 5.7, 1.208],
 ['NITROMETHANE', 101.2, -28.5, 1.131],
 ['PENTANE', 36.1, -129.7, 0.626],
 ['PHENOL', 181.8, 40.9, 1.066],
 ['PROPANENITRILE', 97.1, -92.8, 0.782],
 ['PROPIONIC ACID', 141.1, -20.7, 0.993],
 ['PROPIONITRILE', 97.4, -92.8, 0.782],
 ['PROPYLENE GLYCOL', 187.6, -60.1, 1.04],
 ['PYRIDINE', 115.4, -41.6, 0.978],
 ['SULFOLANE', 287.3, 28.5, 1.262],
 ['TETRAHYDROFURAN', 66.2, -108.5, 0.887],
 ['TOLUENE', 110.6, -94.9, 0.867],
 ['TRIETHYL PHOSPHATE', 215.4, -56.4, 1.072],
 ['TRIETHYLAMINE', 89.5, -114.7, 0.726],
 ['TRIFLUOROACETIC ACID', 71.8, -15.3, 1.489],
 ['WATER', 100.0, 0.0, 1.0],
 ['XYLENES', 139.1, -47.8, 0.86]]

root = tk.Tk()
root.title("ttk.TreeView() to manage solvents")

mc_listbox = MultiColumnListBox()

root.mainloop()
