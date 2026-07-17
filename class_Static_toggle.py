''' class_Static_toggle.py

A class to allow you to toggle between True and False.
Uses decorator @classmethod to call Static.toggle().


tested using Linux and Spyder IDE  vegaseat  17jul2026
'''

class Static:
    """toggle between True and False with each class method call"""
    flag = False
    # decorator allows you to simply call Static.toggle()
    @classmethod
    def toggle(self):
        self.flag = not self.flag
        return self.flag

# testing
for k in range(6):
    print("{}) flag = {}".format(k+1, Static.toggle()))

"""
1) flag = True
2) flag = False
3) flag = True
4) flag = False
5) flag = True
6) flag = False
"""