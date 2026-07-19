''' pqt6_color_bg1.py

testing the PyQT GUI toolkit
use QColor(r, g, b).name() and setStyleSheet(format_string)
to set the background color of the specified widget

here the form's background color is done with a style sheet
this does affect the widgets on top of the form

Use
#rrggbb string eg. red = "#ff0000"

via rgbmixer.exe HTML ...
aqua = #00FFFF
blue = #0000FF
brown = #A52A2A
bisque = #FFE4C4
crimson = #DC143C
cyan = #00FFFF
darkgreen = #006400
gold = #FFD700
green = #008000
lime = #00FF00
magenta = #FF00FF
maroon = #800000
moccasin = #FFE4B5
navy = #000080
orchid = #DA70D6
olive = #808000
orange = #FFA500
pink = #FFC0CB
plum = #DDA0DD
purple = #800080
red = #FF0000
salmon = #FA8072
tan = #D2B48C
teal = #008080
tomato = #D2B48C
turquoise = #40E0D0
violet = #EE82EE
yellow = #FFFF00


or r,g,b values 0 - 255
red = QColor(255, 0, 0).name()
or (try a color name)
QColor("colorName").name()   # gives HTML hex string
print(QColor.colorNames())   # list of 148 predefined colors

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
        self.setWindowTitle("show background color")

        # background colors can be set via a style command
        # this is the format string of the command
        # use % specifier (Python {} format does not work)
        # QWidget works for most widgets that are part of QWidget
        bgString = "QWidget { background-color: %s }"
        # for color use string #rrggbb eg. yellow --> #ffff00
        bgYellow =  bgString % "#ffff00"
        # set the background color of the form
        self.setStyleSheet(bgYellow)

        # create a widget to display the color in
        self.display = QWidget(self)
        self.display.setGeometry(0, 0, 50, 50)

        btnRed = QPushButton("Red")
        bgWhite = "QPushButton { background-color: #ffffff }"
        btnRed.setStyleSheet(bgWhite)
        # bind the button click to a function reference
        btnRed.clicked.connect(self.setRed)

        btnGreen = QPushButton("LimeGreen")
        btnGreen.setStyleSheet(bgWhite)
        # bind the button click to a function reference
        btnGreen.clicked.connect(self.setGreen)

        btnBlue = QPushButton("Blue")
        btnBlue.setStyleSheet(bgWhite)
        # bind the button click to a function reference
        btnBlue.clicked.connect(self.setBlue)

        btnGold = QPushButton("Gold")
        btnGold.setStyleSheet(bgWhite)
        # bind the button click to a function reference
        btnGold.clicked.connect(self.setGold)

        # use a grid layout for the widgets
        grid = QGridLayout()
        # addWidget(widget, row, column, rowSpan=1, columnSpan=1)
        # display spans 4 rows
        grid.addWidget(self.display, 0, 1, 4, 1)
        grid.addWidget(btnRed, 0, 0)
        grid.addWidget(btnGreen, 1, 0)
        grid.addWidget(btnBlue, 2, 0)
        grid.addWidget(btnGold, 3, 0)
        # finalize the layout
        self.setLayout(grid)

    def setRed(self):
        # QColor(r, g, b)
        # name() function returns the color in required format "#rrggbb"
        red = QColor(255, 0, 0).name()
        sf = "QWidget { background-color: %s }" % red
        self.display.setStyleSheet(sf)

    def setGreen(self):
        # use a predefined color name
        green = QColor("limegreen").name()
        sf = "QWidget { background-color: %s }" % green
        self.display.setStyleSheet(sf)

    def setBlue(self):
        blue = QColor(0, 0, 255).name()
        sf = "QWidget { background-color: %s }" % blue
        self.display.setStyleSheet(sf)

    def setGold(self):
        gold = "#FFD700"
        sf = "QWidget { background-color: %s }" % gold
        self.display.setStyleSheet(sf)


app =  QApplication([])
form = MyForm()
form.show()
sys.exit(app.exec())

# extra
# pqt predefined color names...
for color in QColor.colorNames():
    print(color)

''' pqt predefined colors
aliceblue
antiquewhite
aqua
aquamarine
azure
beige
bisque
black
blanchedalmond
blue
blueviolet
brown
burlywood
cadetblue
chartreuse
chocolate
coral
cornflowerblue
cornsilk
crimson
cyan
darkblue
darkcyan
darkgoldenrod
darkgray
darkgreen
darkgrey
darkkhaki
darkmagenta
darkolivegreen
darkorange
darkorchid
darkred
darksalmon
darkseagreen
darkslateblue
darkslategray
darkslategrey
darkturquoise
darkviolet
deeppink
deepskyblue
dimgray
dimgrey
dodgerblue
firebrick
floralwhite
forestgreen
fuchsia
gainsboro
ghostwhite
gold
goldenrod
gray
green
greenyellow
grey
honeydew
hotpink
indianred
indigo
ivory
khaki
lavender
lavenderblush
lawngreen
lemonchiffon
lightblue
lightcoral
lightcyan
lightgoldenrodyellow
lightgray
lightgreen
lightgrey
lightpink
lightsalmon
lightseagreen
lightskyblue
lightslategray
lightslategrey
lightsteelblue
lightyellow
lime
limegreen
linen
magenta
maroon
mediumaquamarine
mediumblue
mediumorchid
mediumpurple
mediumseagreen
mediumslateblue
mediumspringgreen
mediumturquoise
mediumvioletred
midnightblue
mintcream
mistyrose
moccasin
navajowhite
navy
oldlace
olive
olivedrab
orange
orangered
orchid
palegoldenrod
palegreen
paleturquoise
palevioletred
papayawhip
peachpuff
peru
pink
plum
powderblue
purple
red
rosybrown
royalblue
saddlebrown
salmon
sandybrown
seagreen
seashell
sienna
silver
skyblue
slateblue
slategray
slategrey
snow
springgreen
steelblue
tan
teal
thistle
tomato
transparent
turquoise
violet
wheat
white
whitesmoke
yellow
yellowgreen

'''