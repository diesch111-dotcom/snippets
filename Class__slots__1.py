''' Class__slots__1.py
new class style inherits object, the base class that is at
the top of any inheritance tree.  It also allows the use
of __slots__ to restrict class variable creation outside
the class
in addition __slots__ improves the speed of a class by
about 20% replacing the usual class __dict__
works with Python25 and Python31
Starting with Python3 all classes are new style whether
you use (object) or not

Note: you cannot inherit a slot_class in a regular class!
Later versions of python (eg 3.8.5) have a decorator option
@dataclass(slots=true) to avoid the register part

vars() function would return the __dict__ attribute of an instance

works with LinuxMint and Spyder IDE  dns(vegaseat)  15jun2026
'''

# shows methods inherited from object
print(dir(object))


class Oldstyle:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
        print(self.__dict__)  # {'a': 1, 'c': 3, 'b': 2}


class Newstyle(object):
    """
    __slots__ prevents new variable creation outside the class
    and improves the speed by replacing the usual class __dict__
    notice double underlines
    object argument not needed in Python3
    """
    # 'register' the variables allowed
    __slots__ = ["a", "b", "c"]
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
        #print(self.__dict__)  # will give error

class Newstyle2():
    """
    __slots__ prevents new variable creation outside the class
    and improves the speed by replacing the usual class __dict__
    notice double underlines
    note: object argument not needed in Python3
    """
    # 'register' the variables allowed
    __slots__ = ["a", "b", "c"]
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3


oldobj = Oldstyle()
# allows creation of a new class variable outside the class
oldobj.d = 4

print(oldobj.__dict__)  # {'a': 1, 'c': 3, 'b': 2, 'd': 4}

newobj = Newstyle()
# attempt to create a new class variable outside the class
# gives an error, since d is not 'registered'
#newobj.d = 4

# this will fail too since __slots__ has replaced __dict__
#print(newobj.__dict__)

print(newobj.__slots__)  # ['a', 'b', 'c']
print(newobj.a)          # 1

# tests ...
newobj2 = Newstyle2()
print(newobj2.__slots__)  # ['a', 'b', 'c']
