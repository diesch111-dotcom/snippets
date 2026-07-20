''' PG_sound_tk2.py

Click a button to play sound and stop sound
The pygame module handles the sound for tkinter
Will play  MP3, WAV, OGG, MIDI etc.

If you need the optiom to stop the play use
def play2(sound)
def stop(sound)

docs
https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/shipman/button.html

if you need to install pygame ,,,
in the Linux terminal type:
sudo apt-get install python3-pygame  

curious fact:
in the LinuxMint terminal type:  python3 -m tkinter
to get a small tkinter window showing the version of tkinter you have

tested with LinuxMint and Spyder IDE  dns aka vegaseat  17jun2026
'''

import pygame as pg
import tkinter as tk
import os


def play1(sound):
    """
    will load the whole sound into memory before playback
    sound.stop() will not work in this case
    """
    clock = pg.time.Clock()
    sound.play()
    # how often to check active playback
    frame_rate = 30
    while pg.mixer.get_busy():
        clock.tick(frame_rate)
        
def play2(sound):
    """
    less frills, but can stop
    """
    sound.play()

def stop(sound):
    """
    will stop play2()
    """
    sound.stop()


root = tk.Tk()
root.title("pick a button to play a sound via pygame")
# background color of the root window
root['bg'] = 'gold'

#LinuxMint:
os.chdir("/home/dietrich/Music/sound")

# pick a wave sound file you have MP3, WAV, OGG, MIDI etc.
# Linux filenames are case sensitive
# comment out filenames as needed, will play last uncommented file
#sound_file = ""
sound_file = "Mir ham's vom Sauerkraut.mp3"
sound_file = "ChancesAre.MID"
#sound_file = "DingDong.wav"
sound_file = "thunder.wav"
sound_file = "nono.wav"

FREQ = 18000   # play with this for best sound
BITSIZE = -16  # here unsigned 16 bit
CHANNELS = 2   # 1 is mono, 2 is stereo
BUFFER = 1024  # audio buffer size, number of samples
pg.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)
# the code above makes a good sound, for less quality use just
#pg.mixer.init()

# get the sound object
sound = pg.mixer.Sound(sound_file)

# use lambda to send the sound argument to function play
# width is in letters for strings and pixels for image
b1 = tk.Button(text="play1", width=10, command=lambda: play1(sound))
b2 = tk.Button(root, text="play2", width=10, command=lambda: play2(sound))
b3 = tk.Button(text="stop play2", width=10, command=lambda: stop(sound))

# pack() default is center from top
b1.pack(padx=150, pady=10)
b2.pack(padx=150)
b3.pack(pady=10)

root.mainloop()
