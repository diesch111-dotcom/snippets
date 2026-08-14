#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' class_super2.py

The use of super() in Python classes
references the inherited or superclass (aka. baseclass)

Hard coding super()...
super(Cone, self).__init__(r)

New in Python3.3, avoids hardcoding class names...
super().__init__(r)

tested with VSCodium IDE on LinuxMint OS  VegasEat 14aug2026
'''

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        pi = 355/113.0  # approximation of pi
        area = pi * self.r**2
        print("Circle of radius {} has area of {:0.2f}".format(self.r, area))
        return area

circle = Circle(r=4)


class Cone(Circle):
    """
    class Cone inherits class Circle
    """
    def __init__(self, r, h):
        # call the base/super class constructor ...
        #super(Cone, self).__init__(r)
        # new in Python3.3, avoids hardcoding class names
        super().__init__(r)
        self.r = r
        self.h = h

    def volume(self):
        # notice how to call the method of class Circle
        vol = 1.0/3 * self.h * Circle.area(self)
        sf = "Cone of height = %s and radius = %s has volume = %0.2f"
        print(sf % (self.h, self.r, vol))


cone = Cone(r=4, h=10)
cone.volume()

'''result...
Circle of radius 4 has area of 50.27
Cone of height = 10 and radius = 4 has volume = 167.55
'''

