''' class_inspect_signature.py
get the variables that a class instance needs
also namedtuple instance


works with LinuxMint and Spyder IDE  dns(vegaseat)  15jun2026
'''

import inspect

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

print(inspect.signature(Stock))

''' result ...
(name, shares, price)
'''