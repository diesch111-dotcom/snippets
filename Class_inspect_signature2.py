#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Class_inspect_signature2.py

Get the variables that a class instance needs

VegasEat  12oct2026
'''

import inspect
from dataclasses import dataclass

class Patient:
    # a standard class construct
    def __init__(self, ID, name, sex, age, address, phone, bdate, height, weight):
        # assign parameters to the instance self, somewhat combersome
        self.ID = ID
        self.name = name
        self.sex = sex
        self.age = age
        self.address = address
        self.phone = phone
        self.bdate = bdate
        self.height = height
        self.weigh =  weight

    def ask_address(self):
        print("%s do you still live at: %s" % (self.name, self.address))

@dataclass
class PatientDC:
    # the @dataclass decorator simplifies the class construct
    ID: int
    name: str
    sex: chr
    age: int
    address: str
    phone: str
    bdate: str
    height: float
    weight: int

    def ask_address(self):
        print(f"{name} do you still live at: {address}")

# helps when coding a class instance
print(inspect.signature(Patient))  

'''
(ID, name, sex, age, address, phone, bdate, height, weight)
'''

# helps when coding a class instance, has type details too
print(inspect.signature(PatientDC))  

'''
(ID: int, name: str, sex: <built-in function chr>, age: int, 
address: str, phone: str, bdate: str, height: float, weight: int) -> None
'''

