#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' clipboard_action_tk2.py

use Tkinter to get access to the clipboard/pasteboard

clipboard_clear()
clipboard_append(text)
clipboard_get()  the text


works with LinuxMint and SublimeText IDE  dns(vegaseat)  15jun2026
'''

import tkinter as tk

root = tk.Tk()
# keep the window from showing
root.withdraw()

text = "Himmel Donnerwetter"
root.clipboard_clear()
# text to clipboard
root.clipboard_append(text)
# text from clipboard
clip_text = root.clipboard_get()

print(clip_text)
'''
Himmel Donnerwetter
'''

#help(root.clipboard_get)
