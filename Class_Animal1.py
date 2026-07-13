''' Class_Animal1.py
a look at a simple Python class

a class combines methods/functions that belong together
to keep methods private, prefix with a double underline only

the @dataclass decorator simplifies the class construct
vars() function returns the __dict__ attribute of an instance

btw: I love to eat out in LV hence the name vegas eat

works with LinuxMint and Spyder IDE  dns aka vegaseat  15jun2026
'''

# needs Python 3.7+
from dataclasses import dataclass
import inspect

# earlier way without @dataclass decorator
class Animal:
    """
    class names by convention are capitalized
    """
    def __init__(self, animal, sound):
        """
        __init__() is the 'constructor' of the class instance
        when you create an instance of Animal you have to supply
        it with the name and the sound of the animal
        'self' refers to the instance
        if the instance is dog, then
        name and sound will be that of the dog
        'self.' also makes name and sound and methods available
        to all the methods within the class
        """
        self.name = animal
        self.sound = sound

    def speak(self):
        """
        the first argument of a class method is always self
        this method needs to be called with self.speak() within
        the class, or the instance_name.speak() outside the class
        """
        print("The {} goes {}".format(self.name, self.sound))

    # subs for print(instance)
    def __repr__(self):
        # the first argument of a class method is always self
        return f"I am a {self.name} and go {self.sound}"

# the @dataclass decorator simplifies the class construct
@dataclass
class Animal2:
    name: str
    sound: str
 
    def speak(self):
        print(f"The {self.name} goes {self.sound}")
    
    # subs for print(instance)
    def __repr__(self):
        # the first argument of a class method is always self
        return f"I am a {self.name} and go {self.sound}"
        

# helps when coding a class instance
print(inspect.signature(Animal2))  
# (name: str, sound: str) -> None
print("="*40)
# create a few class instances
# remember to supply the name and the sound for each animal
dog = Animal2("dog", "woof")
cat = Animal2("cat", "meeouw")
cow = Animal2("cow", "mooh")

print(dog)  # I am a dog and go woof
print(cat)  # I am a cat and go meeouw

# vars() function returns the __dict__ attribute of an instance
print(vars(dog))  # {'sound': 'woof', 'name': 'dog'}
print(vars(cat))  # {'name': 'cat', 'sound': 'meeouw'}
print(vars(cow))  # {'name': 'cow', 'sound': 'mooh'}

print("="*40)

# you can also access variables associated with the instance
cow.speak()       # The cow goes mooh
print(cow.sound)  # mooh

