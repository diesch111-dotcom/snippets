#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' button_font_color_RandomSentences_tk1.py

Run this program on your Python machine if you want 'informative'
information every now and then to smile.

Displays random sentences from a list using Tkinter GUI tk.Button().
Button expands to fit the text.

Some examples of common fonts:
(family, size, weight)  'normal' weight is the default
arial25n = ['Arial', 25]
cour20b = ('courier', 20, 'bold')
cosa24b = ('Comic Sans MS', 24, 'bold')
helv16b = ('helvetica', 16, 'bold')
helv20bi = ('helvetica', 20, 'bold italic')
times20b = ('times', 20, 'bold')
times12n = ('times', 12, 'normal')
verd20bi = ('verdana', 20, 'bold italic')

docs
https://tkdocs.com/shipman/button.html
https://tkdocs.com/shipman/colors.html


tested using the Spyder IDE on Linux OS  dns(vegaseat)  10jul2026
'''

# python3
import tkinter as tk
import random

# seed the random generator (default is from system time)
random.seed()

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
'Tkinter does stands for Tool Kit interface,',
'I keep forgetting that I forgot about you.',
'I still miss you Baby, but my aim is getting better!',
'A Cursor is someone who swears.',
'A Hard Drive is getting home in the winter,',
'Is reading in the bathroom considered Multi-Tasking?',
'What boots up must come down.',
'There are more chickens than people in the world.' 
]

def set_text():
    str = random.choice(sentence_list)
    button.config(text=str)
    
#create the main form
root = tk.Tk()
# set the form's title
root.title('Click on button text area')
x = 25
y = 20
# only set upper left corner ULC (x, y) position of root window
root.geometry(f"+{x}+{y}")

# create a button
mytext = 'Click to set new text ...'
button = tk.Button(
    root, 
    text=mytext, 
    height=3,
    font=('Comic Sans MS', 24, 'bold'),
    fg='black',
    bg='yellow',
    bd=10,
    relief='raised',
    command=set_text)

# position the button, it expands with the text
button.pack(expand='yes', fill='both')

# start the event loop (run the program)
root.mainloop()
