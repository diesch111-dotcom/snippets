''' class_airlineticket.py

A typical class applcation simplfied with a dataclass decorator


tested using Linux and Spyder IDE  vegaseat  17jul2026
'''

# needs Python 3.7+
from dataclasses import dataclass


# hormal class construct
class AirlineTicket:
    # by convention capitalize class names
    def __init__(self, name, orig, dest, travel_date, travel_class, price):
        # assign parameters to the instance self
        self.name = name
        self.orig = orig
        self.dest = dest
        self.travel_date = travel_date
        self.travel_class = travel_class
        self.price = price

    def info(self):
        # format the info string
        info_str = " {} travels {} class\n from {} to {} on {}"
        info = info_str.format(self.name, self.travel_class, self.orig,
                           self.dest, self.travel_date)
        return info


# the @dataclass decorator simplifies the class construct
@dataclass
class AirlineTicket2:
    # by convention capitalize class names
    name: str 
    orig: str 
    dest: str 
    travel_date: str 
    travel_class: str 
    price: float

    def info(self):
        # format the info string
        info_str = " {} travels {} class\n from {} to {} on {}"
        info = info_str.format(self.name, self.travel_class, self.orig,
                           self.dest, self.travel_date)
        return info


# AirlineTicket(name, orig, dest, travel_date, travel_class, price)
# have enter all data
name = "Stew Pitt"
orig = "JFK"
dest = "LAX"
travel_date = "12/23/2026"
travel_class = "first"
price = 1820.50

# create unique instance for this traveler
spitt = AirlineTicket2(name, orig, dest, travel_date, travel_class, price)

# test this instance
print(spitt.info())

'''
 Stew Pitt travels first class
 from JFK to LAX on 12/23/2026
'''

print("="*40)

# might be helpfull info
print(vars(spitt))

'''
{'name': 'Stew Pitt', 'orig': 'JFK', 'dest': 'LAX', 
 'travel_date': '12/23/2026', 'travel_class': 'first', 'price': 1820.5}
'''
