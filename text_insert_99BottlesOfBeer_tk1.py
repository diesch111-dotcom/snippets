''' text_insert_99BottlesOfBeer_tk1.py
add '99 bottles of beer' lyrics to a Tkinter tk.Text() edit area

use the mouse wheel to scroll text

tk.Text() works like a simple editor ...
highlight/select text by dragging cursor over it
use ctrl+c to copy, ctrl+x to cut selected text,
ctrl+v to paste, and ctrl+a to select all

indexing syntax ...
'1.0' means line 1 first character start (column=0)
'1.20' means line1 20th character (column=20)
to delete first 20 characters from line 1 use
text1.delete('1.0', 1.20')

to insert new text from start of line 1 use
text1.insert('1.0', 'some text')
or add to the end of existing text use
text1.insert('end', 'some text')

to scroll to line 460 use
text1.see('460.0')

to show the text from start of line 27 to start of line 31 use
print(text1.get('27.0', '31.0'))

if you know a person that does not know the full lyrics of this famous
song, run this code so they can learn it
introducing a large font might help

tested using LinuxMint and the Spyder IDE  dns(vegaseat)  4jul2026
'''

import tkinter as tk

root = tk.Tk()
root.title('tk.Text() 99 Bottles of Beer')

# width and height depend on character size
text1 = tk.Text(root, width=35, height=30, bg='tan')
text1.pack()
# start of line 1 is indexed as '1.0' (means 'row.column')
text1.insert('1.0', '   (scroll with mouse wheel)')

# create the '99 bottles of beer' lyrics with a for loop
bottle = "\n%s bottle"
beer = "s of beer on the wall!"
take = "!\nTake one down, pass it around,"
text = ""
for k in range(99, 0, -1):
    # an exercise in slicing
    s1 = ((bottle % k + beer[k==1:])*2)[:-13]
    s2 = bottle % (k-1 or "No")
    s3 = beer[k==2:-1] + "!"
    text = s1 + take + s2 + s3 + "\n"
    # you can use 'end' to keep adding to the end of existing text
    text1.insert('end', text)

# eg. scroll to line 460
#text1.see('460.0')

root.mainloop()
