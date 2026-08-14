#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' PG_tk_sound_panel.py

Run several sounds at the same time with different volumes,
using tkinter and pygame (they coexist peacefully)

tk.Checkbutton()
tk.Scale()
pygame.mixer

In the LinuxMint terminal try:
sudo apt-get install python3-pygame

tested with IDLE IDE on LinuxMint  VegasEat 19jul2026
'''

import tkinter as tk
import pygame.mixer


class SoundPanel(tk.Frame):
    def __init__(self, parent, mixer, sound_file):
        tk.Frame.__init__(self, parent)
        self.track = mixer.Sound(sound_file)
        self.track_playing = tk.IntVar()

        track_button = tk.Checkbutton(self, variable=self.track_playing,
            command=self.track_toggle, text=sound_file)
        track_button.pack(side='left')
        self.volume = tk.DoubleVar()
        self.volume.set(self.track.get_volume())
        volume_scale = tk.Scale(self, variable=self.volume,
            from_=0.0, to=1.0,
            resolution=0.1, command=self.change_volume,
            label="Volume", orient='horizontal')
        volume_scale.pack(side='right')

    def track_toggle(self):
        if self.track_playing.get() == 1:
            self.track.play(loops = -1)
        else:
            self.track.stop()

    def change_volume(self, v):
        self.track.set_volume(self.volume.get())

# test the module
if __name__ == '__main__':
    # pick a sound file you have in the working folder
    # or supply full path
    soundfile1 = "../sound/Chimes.wav"
    soundfile2 = "../sound/DingDong.wav"

    # create main window
    root = tk.Tk()
    root.title("Sound Mixer")

    # set up the pygame mixer
    mixer = pygame.mixer
    mixer.init()

    # create instances
    panel1 = SoundPanel(root, mixer, soundfile1)
    panel1.pack()
    panel2 = SoundPanel(root, mixer, soundfile2)
    panel2.pack()

    def shutdown():
        # self.track is a variable in class SoundPanel and
        # needs to be associated with the proper instance
        panel1.track.stop()
        panel2.track.stop()
        root.destroy()

    # shut it down orderly
    root.protocol("WM_DELETE_WINDOW", shutdown)
    # run the event loop
    root.mainloop()
