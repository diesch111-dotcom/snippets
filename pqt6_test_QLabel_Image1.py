''' pqt6_test_QLabel_Image1.py

test PyQt5 widgets
show QLabel with a QPixmap image on it

If need be use the Linux Software Manager to install Python3-pyqt6

tested ++ using the Spyder IDE on Linux OS  dns aka vegaseat  13jul2026
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
image_file = "/home/dietrich/AAtest_py/image/jpg/PorscheBoxster.jpg"
image = QPixmap(image_file)

# QLabel adjusts to size of image
label = QLabel()
label.setPixmap(image)
label.show()

# ---- end of widget test code -----

import sys
sys.exit(app.exec())
