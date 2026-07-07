''' class_inspect_signature.py
get the variables that a class instance needs
also check what the @dataclass decorator does


using the Spyder IDE on Linux  dns(vegaseat) 7jul2026
'''

import inspect
# needs Python 3.7+
from dataclasses import dataclass


# earlier way without @dataclass decorator
class Stock:
    def __init__(self, symbol, shares, price):
        self.symbol = symbol
        self.shares = shares
        self.price = price
        
    # subs for print(instance)
    def __repr__(self):
        # the first argument of a class method is always self
        val = self.price * self.shares
        return f"{self.shares} shares of {self.symbol} value is ${val:,.2f}"



# the @dataclass decorator simplifies the class construct
@dataclass
class Stock2:
    symbol: str
    shares: int 
    price: float 
    
    # subs for print(instance)
    def __repr__(self):
        # the first argument of a class method is always self
        val = self.price * self.shares
        return f"{self.shares} shares of {self.symbol} value is ${val:,.2f}"
    

# helps when coding a class instance
print(inspect.signature(Stock2))  
# (symbol: str, shares: int, price: float) -> None
print("="*40)
# create class instances
stock_INTC = Stock2("INTC", 100, 127.86) 
stock_GEV = Stock2("GEV", 100, 979.07)

print(stock_INTC) # 100 shares of INTC value is $12,786.00
print(stock_GEV)  # 100 shares of GEV value is $97,907.00 

