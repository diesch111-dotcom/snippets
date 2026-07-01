''' background_deco2.py
running a function in the background with threading
apply threading to a function with a function decorator
the background decorated functions print in the delay order
similar to goroutines in GO language

notice:
the online C compiler on LinuxMint Firefox also runs Python3 
(select Python 3 from dropdown menu in upper left corner)

LinuxMint with Python3-all and SUBLIME IDE works great
dns (vegaseat)  29apr2026

shared: https://onlinegdb.com/NDrghjMZXu
'''

import time
import threading
import functools

def background(funk):
    """
    create a threading decorator
    use @background above the function you want to thread
    (run in the background)
    the wraps decorator makes debugging funk() easier
    """
    @functools.wraps(funk)
    def bg_funk(*a, **kw):
        threading.Thread(target=funk, args=a, kwargs=kw).start()
    return bg_funk

# notice the decorator starting with @
@background
def awake(name, delay):
	time.sleep(delay)
	print(name, "is awake!")

	
print("Now come the background functions ...")

# call backround functions awake(name, delay in seconds)
# results come in depending on delay set
# "Sweet Abby" first, then "Tiptoe Tom" and so on ...
awake("Bearded Bob", 8)
awake("Sweet Abby", 1)
awake("Jolly Jane", 5)
awake("Tiptoe Tom", 2)
awake("Sleepy Joe", 12)

# give the background functions enough time to finish before exiting	
time.sleep(15)

''' result ...
Now come the background functions ...
Sweet Abby is awake!
Tiptoe Tom is awake!
Jolly Jane is awake!
Bearded Bob is awake!
Sleepy Joe is awake!
[Finished in 15.1s]
'''
