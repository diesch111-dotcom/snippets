#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_Hello3.py

Applying a font, color, border and a timer to a QLabel
Used a class to keep it all together
building info...
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtCore import QTimer, Qt

self.

QLabel in PyQt6 doesn't have a built-in clicked signal like QPushButton

tested with VSCodium IDE on LinuxMint  VegasEat 22aug2026
'''

import sys
# consider wildcard imports to be initially okay with pyqt
# name conflicts are limited because of the consistent 'Q' prefix of widgets
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import random

# seed the random generator (default is from system time)
random.seed()

class MyLabel(QWidget):
    # inherits QWidget (needed for timing)
    def __init__(self, sentence_list):
        super().__init__()
        self.sentence_list = sentence_list
        # setGeometry(x_pos, y_pos, width, height)
        #self.setGeometry(100, 150, 320, 100)
        self.text = 'Take a diuretic to see if it works!'
        self.label = QLabel(self.text)
        # apply a font
        font = QFont("Times", 40)
        self.label.setFont(font)
        # center text (horizontally and vertically)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # use frame box styling for a cute border
        self.label.setFrameShape(QFrame.Shape.Box)
        self.label.setFrameShadow(QFrame.Shadow.Raised) # Options: Raised, Sunken, Plain
        self.label.setLineWidth(4)
        # set the foreground and background colors of the label
        # the label text is considered foreground 
        fg = "QLabel {color:red}"
        bg = "QLabel {background-color:yellow}"
        # apply with a style sheet
        self.label.setStyleSheet( fg+bg )
        # Set a fixed size (width, height)
        self.label.setFixedSize(1400, 80)
        # show your genius effort
        self.label.show()

        # Create the timer object
        self.timer = QTimer(self)
        # connect the timeout signal to a function
        self.timer.timeout.connect(self.label_change_text)
        # start the timer with an interval given in milliseconds
        self.timer.start(20_000)

    def label_change_text(self):
        new_text = random.choice(self.sentence_list)
        self.label.setText(new_text)

  
sentence_list = [
'If a deaf person has to go to court, is it still called a hearing?',
'Yesterday is history, today is reality, tomorrow is a mystery.',
'What disease did cured ham actually have?',
'Coffee is a person who has been coughed upon.',
'What did the zebra do to earn its stripes?',
'Is the opposite of a memory a forgettery?',
'I read the Constitution for the articles.',
'Computer programmers do not byte, they nibble a bit.',
'Door sign at the Microbiology Lab: Staph Only!',
'Prevents tingling and weakness of the extremities.',
'My spouse made me join a bridge club. I jump off next Tuesday.',
'I fought the lawn, and the lawn won.',
'If it is not broken, fix it until it is.',
'Advice is free: The right answer will cost plenty.',
'I feel better after I wine a little.',
'Sex on television cannot hurt you unless you fall off.',
'South Korea has Seoul!',
'You are the reason our kids are so ugly!',
'Upgrade used to be just a steep hill!',
'Micro Chips are left in the bag after you eat the chips.', 
'Am I indecisive? I am not sure!',
'Procrastination is the art of keeping up with yesterday.',
'43.3% of statistics are meaningless!',
'Remember half the people you know are below average.',
'A waist is a terrible thing to mind.',
'Software are those darn plastic knives at fast food chains!', 
'Energizer bunny arrested, charged with battery.',
'Beer: It is not just for breakfast anymore.',
'Airline Virus: You are in Dallas, but your data is in Singapore.',
'A Father is a banker provided by nature.',
'Smile, it is the second best thing you can do with your lips.',
'Beer is now cheaper than gas. Drink, do not drive!',
'Archaeologists will date any old thing.',
'Vegetarian: Native Indian word for lousy hunter.',
'If a train station is where the train stops, what is a work station?', 
'It is no honor to be praised by a fool!',
'Beta is Latin for "still does not work!"',
'Web Site is the home for spiders in the barn and the attic.', 
'If you cannot be replaced, you cannot be promoted!',
'Real Stupidity always beats Artificial Intelligence.',
'Living on Earth does include a free trip around the sun every year.',
'Knowledge is power. Power corrupts. Study hard and be evil!',
'UNIX needs a genius to understand its simplicity.',
'The stupid are sure and the intelligent are full of doubt.',
'Boil the Hell Out Of Water and you get Holy Water!',
'In a real Dictionary divorce comes before marriage.',
'Tkinter does stand for Tool Kit interface,',
'I keep forgetting that I forgot about you.',
'I still miss you Baby, but my aim is getting better!',
'A Cursor is someone who swears.',
'A Hard Drive is getting home in the winter,',
'Is reading in the bathroom considered Multi-Tasking?',
'What boots up must come down.',
'A hole is nothing in something',
'A doe does what does do!',
'There are more chicken than people in the world.' 
]

if __name__ == "__main__":
    app = QApplication([])
    win = MyLabel(sentence_list)
    #win.show()
    # start the application's event loop with app.exec()
    # and allow the window corner x click to exit when done
    sys.exit(app.exec())    