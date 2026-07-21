''' Button_multi_loop_class_tk3.py

Exploring Tkinter buttons
Create multiple buttons using list comprehension
Use a class approach to Tkinter

https://tkdocs.com/tutorial/index.html
https://tkdocs.com/shipman/button.html
https://tkdocs.com/shipman/label.html

tested with LinuxMint and Spyder IDE  vegaseat  20jul2026
'''

from functools import partial
import tkinter as tk

class Gui(tk.Tk):
    def __init__(self):
        # the root will be self
        tk.Tk.__init__(self)
        self.title('left mouse click buttons')
        # width is in characters of the given font
        self.label = tk.Label(self, width=20, bg='pink', fg='blue',
                              font='times 12 bold')
        self.label.pack(padx=50, pady=3)
        self.button_labels = ['red', 'green', 'magenta', 'yellow']
        # create buttons using a list comprehension
        self.buttons = [tk.Button(self, width=20, text=label,
                        command=partial(self.do_command, ix, label)) \
                        for ix, label in enumerate(self.button_labels)]
        #print(self.buttons)  # test
        # lay out the buttons via pack()
        for button in self.buttons:
            button.pack(pady=3)
        # command responds to the left mouse click
        # optionally bind the buttons to an action on
        # clicking the left mouse button
        for ix, button in enumerate(self.buttons):
            button.bind('<Button-1>', partial(self.do_binding, ix))

    def do_command(self, ix, label):
        # test print()
        print('command ix={0} label={1}'.format(ix, label))
        # in this case color info is in label
        self['bg'] = label
        # use index ix to do something from a list
        print(self.buttons[ix])

    def do_binding(self, ix, event):
        # get background color of button clicked
        bg_color = event.widget['bg']
        # test print()
        print('binding ix={0} bg={1}'.format(ix, bg_color))
        # use ix to show current button label
        self.label['text'] = self.button_labels[ix]

    def run(self):
        self.mainloop()


# test the potential module
if __name__ == '__main__':
    Gui().run()
    