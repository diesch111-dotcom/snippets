''' button_font_color_RandomSentences_tk1.py

exploring Tkinter text fonts
display random sentences from a list using tk.Button()
button and root expand automatically to fit the text

Tkinter can use a number of named colors (not case sensitive) like
red, green, blue, white, black, tan, pink, yellow, magenta, lightblue
lightgreen, moccasin, peachpuff, orange, grey, purple, brown
also (light=1 to dark=4) hues of colors like
red1, red2, red3, red4   etc.

tuple examples of common fonts (some might be available just on Windoze?)
(family, size, weight)
times48b = ('times', 48, 'bold')
times20b = ('times', 20, 'bold')
times12n = ('times', 12, 'normal')
cour20b = ('courier', 20, 'bold')
helv20bi = ('helvetica', 20, 'bold italic')
verd20bi = ('verdana', 20, 'bold italic')
cosa24b = ('Comic Sans MS', 24, 'bold')
helv16b = ('helvetica', 16, 'bold')
# 'normal' is default
arial25n = ['Arial', 25]
calibri12bu = ('calibri', 12, 'bold', 'underline')

this would change the font in all the root widgets ...
root.option_add('*Font', ("Helvetica",20))

docs
https://tkdocs.com/shipman/button.html
https://tkdocs.com/shipman/colors.html


tested using the Spyder IDE on Linux  dns(vegaseat)  9jul2026
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
'Is the opposite if a memory a forgettery?',
'I read the Constitution for the articles.',
'Door sign at the Microbiology Lab: Staph Only!',
'I fought the lawn, and the lawn won.',
'If it is not broken, fix it until it is.',
'Advice is free: The right answer will cost plenty.',
'I feel better after I wine a little.',
'Sex on television cannot hurt you unless you fall off.',
'South Korea has Seoul!',
'Am I indecisive? I am not sure!',
'Procrastination is the art of keeping up with yesterday.',
'43.3% of statistics are meaningless!',
'Remember half the people you know are below average.',
'A waist is a terrible thing to mind.',
'Energizer bunny arrested, charged with battery.',
'Beer: It is not just for breakfast anymore.',
'Smile, it is the second best thing you can do with your lips.',
'Beer is now cheaper than gas. Drink, do not drive!',
'Archaeologists will date any old thing.',
'Vegetarian: Native Indian word for lousy hunter.',
'It is no honor to be praised by a fool!',
'If you cannot be replaced, you cannot be promoted!',
'Real Stupidity always beats Artificial Intelligence.',
'Living on Earth does include a free trip around the sun every year.',
'Knowledge is power. Power corrupts. Study hard and be evil!',
'UNIX needs a genius to understand its simplicity.',
'The stupid are sure and the intelligent are full of doubt.',
'Boil the Hell Out Of Water and you get Holy Water!'
]

def setText():
    s = random.choice(sentence_list)
    button.config(text=s)
    
#create the main form
root = tk.Tk()
# set the form's title
root.title('Click on text area')
x = 25
y = 20
# only set upper left corner ULC (x, y) position of root window
root.geometry(f"+{x}+{y}")

# create a button
mytext = 'Click to set new text ...'
button = tk.Button(root, text=mytext, command=setText)

myfont = ('Comic Sans MS', 24, 'bold') 

# configure the button's text font and foreground/background colors
button.config(height=3, font=myfont, fg='black', bg='yellow')
# more options
button.config(relief='raised', bd=10)

# pack the button
button.pack(expand='yes', fill='both')

# start the event loop (run the program)
root.mainloop()
