#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_test_QLabel_Image1.py

Test PyQt5 widgets
Show QLabel with a QPixmap image on it

If need be use the Linux Software Manager to install Python3-pyqt6

tested with Spyder IDE on LinuxMint  VegasEat 19jul2026
'''

# for Qt
#from PyQt6.QtCore import *
# for QColor, QPainter, QIcon, QPixmap etc
from PyQt6.QtGui import *
# for QSound, MacOS installation lacks QtMultimedia
#from PyQt6.QtMultimedia import *
# for QWidget, QPushButton, QLabel etc
from PyQt6.QtWidgets import *


app = QApplication([])

# ----- start your widget test code ----

# the image file can be a .jpg, .png, ,gif, .bmp image file
# if not in the working directory, give the full path ...
image_file = "/home/admin123/Pictures/image/jpg/PorscheBoxster.jpg"
image = QPixmap(image_file)

# QLabel adjusts to size of image
label = QLabel()
label.setPixmap(image)
label.show()

# ---- end of widget test code -----

import sys
sys.exit(app.exec())
