''' class_airlineticket.py

A typical class applcation


tested using Linux and Spyder IDE  vegaseat  17jul2026
'''

class AirlineTicket:
    # by convention capitalize class names
    def __init__(self, name, orig, dest, travel_date, travel_class, price):
        # assign parameters to the instance self
        self.name = name
        self.origination = orig
        self.destination = dest
        self.travel_date = travel_date
        self.travel_class = travel_class
        self.price = price

    def info(self):
        # format the info string
        info_str = " {} travels {} class\n from {} to {} on {}"
        info = info_str.format(self.name, self.travel_class, self.origination,
                           self.destination, self.travel_date)
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
spitt = AirlineTicket(name, orig, dest, travel_date, travel_class, price)

# test this instance
print(spitt.info())

'''
 Stew Pitt travels first class
 from JFK to LAX on 12/23/2026
'''
