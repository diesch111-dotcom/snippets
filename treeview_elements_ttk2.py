#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" treeview_elements_ttk2.py

Here the ttk.Treeview() widget is configured as a multi-column listbox
with adjustable column width and column-header-click sorting.

It is loaded with an element list established way back in my years as
a scientist

docs
https://docs.python.org/3/library/tkinter.ttk.html
https://tkdocs.com/shipman/ttk-Treeview.html


tested using LinuxMint and Spyder IDE  dns(vegaseat)  8jul2026
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
        self.tree = ttk.Treeview(columns=element_header, show="headings")
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)

        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in element_header:
            self.tree.heading(col, text=col.title(),
                command=lambda co=col: self.sortBy(self.tree, co, 0))
            # adjust the column's width to the header string
            self.tree.column(col, width=tkFont.Font().measure(col.title()))

        for item in element_list3:
            self.tree.insert('', 'end', values=item)

            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                #print(ix, col_w, len(item))
                if self.tree.column(element_header[ix], width=None) < col_w:
                    self.tree.column(element_header[ix], width=col_w)

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


element_header = ["Atom Num", " Symbol", " Name", "Atomic Weight"]
element_list3 = [
 ['1', 'H', 'Hydrogen', '1.008'],
 ['2', 'He', 'Helium', '4.002602'],
 ['3', 'Li', 'Lithium', '6.94'],
 ['4', 'Be', 'Beryllium', '9.0121831'],
 ['5', 'B', 'Boron', '10.81'],
 ['6', 'C', 'Carbon', '12.011'],
 ['7', 'N', 'Nitrogen', '14.007'],
 ['8', 'O', 'Oxygen', '15.999'],
 ['9', 'F', 'Fluorine', '18.998403163'],
 ['10', 'Ne', 'Neon', '20.1797'],
 ['11', 'Na', 'Sodium', '22.98976928'],
 ['12', 'Mg', 'Magnesium', '24.305'],
 ['13', 'Al', 'Aluminium', '26.9815385'],
 ['14', 'Si', 'Silicon', '28.085'],
 ['15', 'P', 'Phosphorus', '30.973761998'],
 ['16', 'S', 'Sulfur', '32.06'],
 ['17', 'Cl', 'Chlorine', '35.45'],
 ['18', 'Ar', 'Argon', '39.948'],
 ['19', 'K', 'Potassium', '39.0983'],
 ['20', 'Ca', 'Calcium', '40.078'],
 ['21', 'Sc', 'Scandium', '44.955908'],
 ['22', 'Ti', 'Titanium', '47.867'],
 ['23', 'V', 'Vanadium', '50.9415'],
 ['24', 'Cr', 'Chromium', '51.9961'],
 ['25', 'Mn', 'Manganese', '54.938044'],
 ['26', 'Fe', 'Iron', '55.845'],
 ['27', 'Co', 'Cobalt', '58.933194'],
 ['28', 'Ni', 'Nickel', '58.6934'],
 ['29', 'Cu', 'Copper', '63.546'],
 ['30', 'Zn', 'Zinc', '65.38'],
 ['31', 'Ga', 'Gallium', '69.723'],
 ['32', 'Ge', 'Germanium', '72.63'],
 ['33', 'As', 'Arsenic', '74.921595'],
 ['34', 'Se', 'Selenium', '78.971'],
 ['35', 'Br', 'Bromine', '79.904'],
 ['36', 'Kr', 'Krypton', '83.798'],
 ['37', 'Rb', 'Rubidium', '85.4678'],
 ['38', 'Sr', 'Strontium', '87.62'],
 ['39', 'Y', 'Yttrium', '88.90584'],
 ['40', 'Zr', 'Zirconium', '91.224'],
 ['41', 'Nb', 'Niobium', '92.90637'],
 ['42', 'Mo', 'Molybdenum', '95.95'],
 ['43', 'Tc', 'Technetium', '97.0'],
 ['44', 'Ru', 'Ruthenium', '101.07'],
 ['45', 'Rh', 'Rhodium', '102.9055'],
 ['46', 'Pd', 'Palladium', '106.42'],
 ['47', 'Ag', 'Silver', '107.8682'],
 ['48', 'Cd', 'Cadmium', '112.414'],
 ['49', 'In', 'Indium', '114.818'],
 ['50', 'Sn', 'Tin', '118.71'],
 ['51', 'Sb', 'Antimony', '121.76'],
 ['52', 'Te', 'Tellurium', '127.6'],
 ['53', 'I', 'Iodine', '126.90447'],
 ['54', 'Xe', 'Xenon', '131.293'],
 ['55', 'Cs', 'Caesium', '132.90545196'],
 ['56', 'Ba', 'Barium', '137.327'],
 ['57', 'La', 'Lanthanum', '138.90547'],
 ['58', 'Ce', 'Cerium', '140.116'],
 ['59', 'Pr', 'Praseodymium', '140.90766'],
 ['60', 'Nd', 'Neodymium', '144.242'],
 ['61', 'Pm', 'Promethium', '145.0'],
 ['62', 'Sm', 'Samarium', '150.36'],
 ['63', 'Eu', 'Europium', '151.964'],
 ['64', 'Gd', 'Gadolinium', '157.25'],
 ['65', 'Tb', 'Terbium', '158.92535'],
 ['66', 'Dy', 'Dysprosium', '162.5'],
 ['67', 'Ho', 'Holmium', '164.93033'],
 ['68', 'Er', 'Erbium', '167.259'],
 ['69', 'Tm', 'Thulium', '168.93422'],
 ['70', 'Yb', 'Ytterbium', '173.054'],
 ['71', 'Lu', 'Lutetium', '174.9668'],
 ['72', 'Hf', 'Hafnium', '178.49'],
 ['73', 'Ta', 'Tantalum', '180.94788'],
 ['74', 'W', 'Tungsten', '183.84'],
 ['75', 'Re', 'Rhenium', '186.207'],
 ['76', 'Os', 'Osmium', '190.23'],
 ['77', 'Ir', 'Iridium', '192.217'],
 ['78', 'Pt', 'Platinum', '195.084'],
 ['79', 'Au', 'Gold', '196.966569'],
 ['80', 'Hg', 'Mercury', '200.592'],
 ['81', 'Tl', 'Thallium', '204.38'],
 ['82', 'Pb', 'Lead', '207.2'],
 ['83', 'Bi', 'Bismuth', '208.9804'],
 ['84', 'Po', 'Polonium', '209.0'],
 ['85', 'At', 'Astatine', '210.0'],
 ['86', 'Rn', 'Radon', '222.0'],
 ['87', 'Fr', 'Francium', '223.0'],
 ['88', 'Ra', 'Radium', '226.0'],
 ['89', 'Ac', 'Actinium', '227.0'],
 ['90', 'Th', 'Thorium', '232.0377'],
 ['91', 'Pa', 'Protactinium', '231.03588'],
 ['92', 'U', 'Uranium', '238.02891'],
 ['93', 'Np', 'Neptunium', '237.0'],
 ['94', 'Pu', 'Plutonium', '244.0'],
 ['95', 'Am', 'Americium', '243.0'],
 ['96', 'Cm', 'Curium', '247.0'],
 ['97', 'Bk', 'Berkelium', '247.0'],
 ['98', 'Cf', 'Californium', '251.0'],
 ['99', 'Es', 'Einsteinium', '252.0'],
 ['100', 'Fm', 'Fermium', '257.0'],
 ['101', 'Md', 'Mendelevium', '258.0'],
 ['102', 'No', 'Nobelium', '259.0'],
 ['103', 'Lr', 'Lawrencium', '262.0'],
 ['104', 'Rf', 'Rutherfordium', '267.0'],
 ['105', 'Db', 'Dubnium', '270.0'],
 ['106', 'Sg', 'Seaborgium', '271.0'],
 ['107', 'Bh', 'Bohrium', '270.0'],
 ['108', 'Hs', 'Hassium', '277.0'],
 ['109', 'Mt', 'Meitnerium', '276.0'],
 ['110', 'Ds', 'Darmstadtium', '281.0'],
 ['111', 'Rg', 'Roentgenium', '282.0'],
 ['112', 'Cn', 'Copernicium', '285.0'],
 ['113', 'Uut', 'Ununtrium', '285.0'],
 ['114', 'Fl', 'Flerovium', '289.0'],
 ['115', 'Uup', 'Ununpentium', '289.0'],
 ['116', 'Lv', 'Livermorium', '293.0'],
 ['117', 'Uus', 'Ununseptium', '294.0'],
 ['118', 'Uuo', 'Ununoctium', '294.0']]


root = tk.Tk()
root.title("ttk.TreeView() to manage elements")

mc_listbox = MultiColumnListBox()

root.mainloop()


