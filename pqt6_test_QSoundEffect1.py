#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_test_QSoundEffect1.py

a very simple template to test PyQT6 widgets
just test QSoundEffect() which replaces  QSoundd()

https://doc.qt.io/qt-5/qtmultimedia-module.html
https://doc.qt.io/qt-5/qsound.html
also
https://doc.qt.io/qt-5/qsoundeffect.html

if needed use the Software Manager (search pyqt6) to install...
Pytho3-pyqt6
Pytho3-pyqt6.qtmultimedia

tested with LinuxMint and SublimeText IDE   vegaseat  19jul2026
'''

from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget

app = QApplication([])

window = QWidget()
window.setGeometry(70, 150, 320, 100)
button = QPushButton("Play Sound", window)
# any of these sound formats .mp3   .wav  .ogg   .mid    
soundffile = "/home/admin123/Music/sound/DingDong.wav"
# Create the sound effect
effect = QSoundEffect(window)  # Passing parent prevents garbage collection!
effect.setSource(QUrl.fromLocalFile(soundffile))
effect.setVolume(0.5)  # Range: 0.0 to 1.0

# Play on click
button.clicked.connect(effect.play)

window.show()
app.exec()
