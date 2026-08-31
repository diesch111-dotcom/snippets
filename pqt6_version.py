#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_version.py

getting the PyQT and its Qt versions

tested with IDLE IDE on LinuxMint  VegasEat 28aug2026
'''

from PyQt6.QtCore import PYQT_VERSION_STR, QT_VERSION_STR

print(f"PyQt6 Version: {PYQT_VERSION_STR}")
print(f"Qt Version:    {QT_VERSION_STR}")

''' eg.
PyQt6 Version: 6.6.1
Qt Version:    6.4.2
'''
