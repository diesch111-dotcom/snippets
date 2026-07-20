''' PG_Playsound2.py

Use the pygame module to play a wave sound file
Can combine this with the tkinter GUI

After fiddling with PyQt6.QtMultimedia.QAudioOutput() this is refreshing!

note that with Linux filenames are case-sensitive
my sound files are in a subdirectory '/home/dietrich/Music/sound' eg.
sound_file = "/home/dietrich/Music/sound/DingDong.wav"
sound_file = "/home/dietrich/Music/sound/thunder.wav"
# MP3 files work too...
sound_file = "/home/dietrich/Music/sound/Drumtrack.mp3"
# so do OGG files
sound_file = "/home/dietrich/Music/sound/DontGetMeWrong.ogg"
# so do MIDI file, might have to bring up the volume a bit
sound_file = "/home/dietrich/Music/sound/CRAZYPAT2.MID"

in the LinuxMint terminal type:
sudo apt-get install python3-pygame  
to get pygame installed if need be

works with the Spyder IDE  on LinuxMint OS    vegaseat  15jun2026
'''

import pygame as pg

def play_sound(sound_file):
    """
    will load the whole sound into memory before playback
    """
    sound = pg.mixer.Sound(sound_file)
    clock = pg.time.Clock()
    sound.play()
    # how often to check active playback
    frame_rate = 30
    while pg.mixer.get_busy():
        clock.tick(frame_rate)


FREQ = 18000   # play with this for best sound
BITSIZE = -16  # here unsigned 16 bit
CHANNELS = 2   # 1 is mono, 2 is stereo
BUFFER = 1024  # audio buffer size, number of samples

#pg.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)
# for less quality sound use just
pg.mixer.init()

# optional volume 0 to 1.0
pg.mixer.music.set_volume(0.8)

# pick a wave (.wav) sound file you have in the working directory
# or give full file path
#sound_file = "/home/dietrich/Music/sound/DingDong.wav"
#sound_file = "/home/dietrich/Music/sound/thunder.wav"
# MP3 files work too...
sound_file = "/home/dietrich/Music/sound/Mir ham's vom Sauerkraut.mp3"
# so do OGG files
#sound_file = "/home/dietrich/Music/sound/DontGetMeWrong.ogg"
# so dd MIDI files, might have to bring up the volume a bit
#sound_file = "/home/dietrich/Music/sound/CRAZYPAT2.MID"

print(f"playing sound file: {sound_file}")

#play_sound(sound_file)
# even simpler
pg.mixer.Sound(sound_file).play()
