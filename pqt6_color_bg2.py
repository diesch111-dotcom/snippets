''' pqt6_color_bg2.py

testing the PyQT GUI toolkit
use QColor(r, g, b).name() and setStyleSheet(format_string)
to set the background color of the specified widget

Also Qt.GlobalColor.red etc. allows for some basic color nmaes
Try to test print them

print(QColor.colorNames())   # list of 148 predefined color names

Here the form background is a paintEvent canvas colored with a brush
does not affect the other widget on top of it

If need be use the Linux Software Manager to install Python3-pyqt6

tested ++ using the Spyder IDE on Linux OS  dns aka vegaseat  13jul2026
'''

# for Qt
from PyQt6.QtCore import *
# for QColor
from PyQt6.QtGui import *
# for QWidget, QPushButton, QLabel, QApplication etc
from PyQt6.QtWidgets import *
import sys


class MyForm(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(100, 150, 320, 100)
        self.setWindowTitle("show background colors")

        # create a widget to display the color in
        self.display = QWidget(self)
        self.display.setGeometry(0, 0, 50, 50)

        btnRed = QPushButton("Red")
        # bind the button click to a function reference
        btnRed.clicked.connect(self.setRed)

        btnGreen = QPushButton("Green")
        # bind the button click to a function reference
        btnGreen.clicked.connect(self.setGreen)

        btnBlue = QPushButton("Blue")
        # bind the button click to a function reference
        btnBlue.clicked.connect(self.setBlue)

        # use a grid layout for the widgets
        grid = QGridLayout()
        # addWidget(widget, row, column, rowSpan=1, columnSpan=1)
        # display spans 3 rows
        grid.addWidget(self.display, 0, 1, 3, 1)
        grid.addWidget(btnRed, 0, 0)
        grid.addWidget(btnGreen, 1, 0)
        grid.addWidget(btnBlue, 2, 0)
        # finalize the layout
        self.setLayout(grid)

    def setRed(self):
        # QColor(r, g, b) values are from 0 to 255
        # name() function returns the color in format "#RRGGBB"
        red = QColor(255, 0, 0).name()
        sf = "QWidget { background-color: %s }" % red
        self.display.setStyleSheet(sf)

    def setGreen(self):
        green = QColor(0, 255, 0).name()
        sf = "QWidget { background-color: %s }" % green
        self.display.setStyleSheet(sf)

    def setBlue(self):
        # use predefined color name
        blue = QColor("blue").name()
        print(blue)  # test gives HTML type value of #0000ff
        sf = "QWidget { background-color: %s }" % blue
        self.display.setStyleSheet(sf)

    def setGold(self):
        # example of HTML type color value
        # got HTML type color value from rgbmixer.exe
        gold = "#FFD700"
        sf = "QWidget { background-color: %s }" % gold
        self.display.setStyleSheet(sf)

    def paintEvent(self, event):
        """
        gets called automatically and sets up a
        canvas as the background for self
        """
        painter = QPainter()
        painter.begin(self)
        # color uses red, green, blue values (0 to 255)
        plum = QColor(221, 160, 221)
        painter.setBrush(QBrush(plum))
        painter.drawRect(event.rect())
        painter.end()


app =  QApplication([])
# testing...
print(Qt.GlobalColor.red)
print(Qt.GlobalColor.yellow)
#print(Qt.GlobalColor.gold)  # AttributeError: 
form = MyForm()
form.show()
sys.exit(app.exec())

