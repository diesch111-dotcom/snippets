#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_test_QLabel_Image2.py

Test PyQt5 widgets
Show QLabel with a QPixmap image on it.
The image is from a web page on the internet.

If need be use the Linux Software Manager to install Python3-pyqt6

VegasEat  03oct2026
'''

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from urllib.request import urlretrieve

app = QApplication([])

# find yourself an image on an internet web page you like
# (MSW: right click on the image, look under properties and copy the address)
# actually a rare find!
#image_url = "http://www.google.com/intl/en/images/logo.gif"

# split a long url such that url2 is also the image file name
url1 = "https://arduinomodules.info/wp-content/uploads/"
url2 = "Arduino_KY-037_connection_diagram-1024x650.png"
image_url = url1 + url2

#image_filename = url2
folder = "/home/admin123/Pictures/"
# optional
image_filename = folder + url2

# retrieve the image from the url and save it to a file 
# named image_filename in the working directory
# or give full file path to another directory/folder
urlretrieve(image_url, image_filename)

print(f"Image saved as {image_filename}")

# ----- start your widget test code ----


image = QPixmap(image_filename)

# QLabel adjusts to size of image
label = QLabel()
label.move(50, 60)
label.setPixmap(image)
label.show()

# ---- end of widget test code -----

app.exec()
