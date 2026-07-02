''' geometry_tk101.py
set position and size of a Tkinter window

more info ...
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/geometry.html
https://tkdocs.com/shipman/geometry.html

curious fact:
in the LinuxMint terminal type:  python3 -m tkinter
to get a small tkinter window showing the version of tkinter you have

tested with LinuxMint and Spyder IDE  dns(vegaseat)  17jun2026
'''

import tkinter as tk

root = tk.Tk()
# shows "... #2" if 2 roots are open
#root = tk.Tk(className="root.geometry()")  # sets title too
# or give it your title this way
root.title("root.geometry()")

# set the root window's height, width and x,y position
# x,y are the upper left corner ULC coordinates 
# in pixels
w = 450
h = 200
x = 50
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry(f"{w}x{h}+{x}+{y}")

# only set ULC (x, y) position of root
#root.geometry(f"+{x}+{y}")

# only set size of root
#root.geometry(f"{w}x{h}")

# make Tk window not resizable, also disables the maximize button
#root.resizable(width=FALSE, height=FALSE)
# or ...
#root.resizable(0, 0)
# root/window can only be stretched along width
root.resizable(width='true', height='false')

# or make root window full screen
#root.state('zoomed')

# give it a colorful frame
frame = tk.Frame(root, bg='green')
frame.pack(fill='both', expand='yes')

# get current geometry info (update required)
root.update()
print(f'{root.geometry() =}')
print(f'{root.winfo_width() =}')
print(f'{root.winfo_height() =}')
print(f'{root.winfo_geometry() =}')
print(f'{root.winfo_x() =}')
print(f'{root.winfo_y() =}')
print(f'{root.winfo_rootx() =}')
print('takes height of title bar into account:')
print(f'{root.winfo_rooty() =}')

print('display screen info:')
print(f'{root.winfo_screenheight() =}')
print(f'{root.winfo_screenwidth() =}')

print('required minimums:')
print(f'{root.winfo_screenmmheight() =}')
print(f'{root.winfo_screenmmwidth() =}')

'''
root.geometry() ='450x200+50+100'
root.winfo_width() =450
root.winfo_height() =200
root.winfo_geometry() ='450x200+50+132'
root.winfo_x() =50
root.winfo_y() =132
root.winfo_rootx() =50
takes height of title bar into account:
root.winfo_rooty() =132
display screen info:
root.winfo_screenheight() =1080
root.winfo_screenwidth() =1920
required minimums:
root.winfo_screenmmheight() =285
root.winfo_screenmmwidth() =508
'''

root.mainloop()

#help(root.geometry)