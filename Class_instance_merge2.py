#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Class_instance_merge2.py

Merging two class instances

vegaseat  15oct2026
'''

class A:
    pass

class B:
    pass

inst_a = A()
inst_b = B()

inst_a.alpha = 333
inst_b.beta = 777

def merge(ob1, ob2):
    """
    an object's __dict__ contains all its
    attributes, methods, docstrings, etc.
    """
    ob1.__dict__.update(ob2.__dict__)
    return ob1

# merge the two class instances into one instance
inst_a = merge(inst_a, inst_b)

# you can delete instance inst_b (optional)
del inst_b

sf = "instance inst_a now has alpha=%s and beta=%s attributes"
print(sf % (inst_a.alpha, inst_a.beta))

'''
instance inst_a now has alpha=333 and beta=777 attributes
'''
