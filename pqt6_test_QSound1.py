''' pqt6_test_QSound1.py

a very simple template to test PyQT widgets
just test QSound, no window is shown
Note: QSound() has been replaced in PyQt6 as the code below shows 

Linux 'Rhythmbox' plays most soundfiles including midi files.

You need to have the much improved PyQt6.QtMultimedia installed separately
Usin the Linux terminal type:
sudo apt-get install python3-PyQt6.QtMultimedia

tested ++ using the Spyder IDE on Linux OS  dns aka vegaseat  13jul2026
'''

from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6.QtWidgets import QApplication
import sys
import os

app = QApplication([])  # no need to import sys

# ----- start your widget test code ----


player = QMediaPlayer()

# In PyQt6, QAudioOutput acts as the output target for QMediaPlayer
audio_output = QAudioOutput()
# Connect output route
player.setAudioOutput(audio_output) 

directory = "/home/dietrich/AAtest_py/sound"
os.chdir(directory) 
# Set audio source and volume
player.setSource(QUrl.fromLocalFile("DingDong.wav"))

# Normalized 0.0 to 1.0 in PyQt6
audio_output.setVolume(0.8)  

player.play()


# ---- end of widget test code -----

sys.exit(app.exec())
