#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Button_config_info_tk2.py

Use config() to show info of a Tkinter widget
as a dictionary of the options

docs
https://tkdocs.com/shipman/button.html

tested using the Spyder IDE on Linux  dns aka vegaseat  13jul2026
'''

import tkinter as tk
import pprint

root = tk.Tk()
# use default position, title, color and size

btn = tk.Button(root, 
    text='Press me to exit!', 
    width=30, 
    bg='red',           
    fg='gold', 
    font=('courier', 12, 'bold'), 
    command=root.destroy)
btn.pack(pady=10)

# shows all the potential options as a dictionary
pprint.pprint(btn.config())

root.mainloop()

'''
{'activebackground': ('activebackground',
                      'activeBackground',
                      'Foreground',
                      <border object: '#ececec'>,
                      '#ececec'),
 'activeforeground': ('activeforeground',
                      'activeForeground',
                      'Background',
                      <color object: '#000000'>,
                      '#000000'),
 'anchor': ('anchor', 'anchor', 'Anchor', <index object: 'center'>, 'center'),
 'background': ('background',
                'background',
                'Background',
                <border object: '#d9d9d9'>,
                'red'),
 'bd': ('bd', '-borderwidth'),
 'bg': ('bg', '-background'),
 'bitmap': ('bitmap', 'bitmap', 'Bitmap', '', ''),
 'borderwidth': ('borderwidth', 'borderWidth', 'BorderWidth', 1, 1),
 'command': ('command', 'command', 'Command', '', '137088180234304destroy'),
 'compound': ('compound',
              'compound',
              'Compound',
              <index object: 'none'>,
              'none'),
 'cursor': ('cursor', 'cursor', 'Cursor', '', ''),
 'default': ('default',
             'default',
             'Default',
             <index object: 'disabled'>,
             'disabled'),
 'disabledforeground': ('disabledforeground',
                        'disabledForeground',
                        'DisabledForeground',
                        <color object: '#a3a3a3'>,
                        '#a3a3a3'),
 'fg': ('fg', '-foreground'),
 'font': ('font',
          'font',
          'Font',
          <font object: 'TkDefaultFont'>,
          'courier 12 bold'),
 'foreground': ('foreground',
                'foreground',
                'Foreground',
                <color object: '#000000'>,
                'gold'),
 'height': ('height', 'height', 'Height', 0, 0),
 'highlightbackground': ('highlightbackground',
                         'highlightBackground',
                         'HighlightBackground',
                         <border object: '#d9d9d9'>,
                         '#d9d9d9'),
 'highlightcolor': ('highlightcolor',
                    'highlightColor',
                    'HighlightColor',
                    <color object: '#000000'>,
                    '#000000'),
 'highlightthickness': ('highlightthickness',
                        'highlightThickness',
                        'HighlightThickness',
                        1,
                        1),
 'image': ('image', 'image', 'Image', '', ''),
 'justify': ('justify',
             'justify',
             'Justify',
             <index object: 'center'>,
             'center'),
 'overrelief': ('overrelief', 'overRelief', 'OverRelief', '', ''),
 'padx': ('padx', 'padX', 'Pad', <pixel object: '3m'>, <pixel object: '3m'>),
 'pady': ('pady', 'padY', 'Pad', <pixel object: '1m'>, <pixel object: '1m'>),
 'relief': ('relief', 'relief', 'Relief', <index object: 'raised'>, 'raised'),
 'repeatdelay': ('repeatdelay', 'repeatDelay', 'RepeatDelay', 0, 0),
 'repeatinterval': ('repeatinterval', 'repeatInterval', 'RepeatInterval', 0, 0),
 'state': ('state', 'state', 'State', <index object: 'normal'>, 'normal'),
 'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', '', ''),
 'text': ('text', 'text', 'Text', '', 'Press me to exit!'),
 'textvariable': ('textvariable', 'textVariable', 'Variable', '', ''),
 'underline': ('underline', 'underline', 'Underline', -1, -1),
 'width': ('width', 'width', 'Width', '0', 30),
 'wraplength': ('wraplength', 'wrapLength', 'WrapLength', 0, 0)}
'''
