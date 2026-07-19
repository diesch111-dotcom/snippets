''' pqt6_test_QSlider.py

A simple template to test PyQT widgets
Test QSlider() with a QLCDNumber() display

used by QSlider.setTickPosition()
QSlider.NoTicks	    Do not draw any tick marks (default)
QSlider.TicksBothSides	Draw tick marks on both sides of the groove
QSlider.TicksAbove	Draw tick marks above the (horizontal) slider
QSlider.TicksBelow	Draw tick marks below the (horizontal) slider
QSlider.TicksLeft	Draw tick marks to the left of the (vertical) slider
QSlider.TicksRight	Draw tick marks to the right of the (vertical) slider

tested ++ using the Spyder IDE on Linux OS  dns aka vegaseat  13jul2026
'''

# wildcards okay for testing...
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

app = QApplication([])
# create the window and set the title
win = QWidget()
# setGeometry(x_pos, y_pos, width, height)
win.setGeometry(70, 150, 340, 100)
win.setWindowTitle('Move slider bar')
#win.setWindowFlags(win.windowFlags()|Qt.WindowStaysOnTopHint)


def changeValue(event=None):
    """show the changing slider value in the LC display"""
    val = slider.value()
    # display the value in the LCD widget
    lcd.display(val)

# create an LC display
lcd = QLCDNumber()

slider = QSlider(Qt.Orientation.Horizontal)
# slider values 0 to 99 in steps of 1 is default
slider.setRange(0, 200)
# initial value = 0 is the default
slider.setValue(50)
# optional indicators
slider.setTickPosition(QSlider.TickPosition.TicksBelow)
slider.setTickInterval(10)

# set to initial value
changeValue()

# use vertical layout
vbox = QVBoxLayout()
vbox.addWidget(lcd)
vbox.addWidget(slider)
win.setLayout(vbox)

# connect the slider to the lcd number in changeValue()
slider.valueChanged.connect(changeValue)

# optional info ...
print(slider.tickPosition())  # aha...  TickPosition.TicksBelow

win.show()

import sys
sys.exit(app.exec())
