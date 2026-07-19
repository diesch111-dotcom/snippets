''' pqt6_test_QTimeLine.py

Testing PyQt's QProgressBar() and QTimeLine()


If need be use use the Linux Software Manager to inststall Python3-pyqt6

tested ++ using the Spyder IDE on Linux OS  dns aka vegaseat  13jul2026
'''

# wildcards okay for testing...
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


app = QApplication([])

# ----- start your widget test code ----

frame = QFrame()

progress_bar = QProgressBar(frame)
progress_bar.setRange(0, 100)

# construct a 10 second timeline with a 'frame' range of 0 - 100
time_line = QTimeLine(10000, frame)
time_line.setFrameRange(0, 100)
time_line.frameChanged[int].connect(progress_bar.setValue)

# clicking the push button will start the progress bar animation
push_button = QPushButton("start progress bar", frame)
push_button.clicked.connect(time_line.start)

vbox = QVBoxLayout()
vbox.addWidget(progress_bar)
vbox.addWidget(push_button)
frame.setLayout(vbox)

frame.show()

# ---- end of widget test code -----

import sys
sys.exit(app.exec())
