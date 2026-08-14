#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' class_inherit2.py

class Teacher and class Student inherit from class SchoolMember
class names are capitalized by convention to aid readability

New in Python3.3, avoids hardcoding class names eg...
super().__init__(name, age)

tested with VSCodium IDE on LinuxMint OS  VegasEat 14aug2026
'''

# the base or super class
class SchoolMember:
    '''represents any school member'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def detail(self):
        '''show name and age, stay on same line'''
        print('Name: %-13s Age:%s' % (self.name, self.age), end=" ")

# use the base class as argument to inherit from
class Teacher(SchoolMember):
    '''represents a teacher'''
    def __init__(self, name, age, subject):
        # super() assigns name, age to self.name, self.age
        super().__init__(name, age)
        self.subject = subject

    def detail(self):
        '''teaches this course'''
        SchoolMember.detail(self)
        print(f"Teaches course: {self.subject}")

class Student(SchoolMember):
    '''represents a student'''
    def __init__(self, name, age, grades):
        # super() assigns name, age to self.name, self.age
        super().__init__(name, age)
        self.grades = grades

    def detail(self):
        '''student grades'''
        SchoolMember.detail(self)
        print(f"Average grades: {self.grades:d}")

# teacher has name age and subject taught
t1 = Teacher('Dr. Schard', 40, 'Beginning Python 101')
# student has name, age and average grade (max 100)
s1 = Student('Abigale Agat', 20, 92)
s2 = Student('Bertha Belch', 22, 65)
s3 = Student('Karl Kuss', 21, 98)
s4 = Student('Tom Tippit', 22, 77)
s5 = Student('Stew Pitt', 20, 88)

print('-'*60)

# list of instances, Teacher t1 and Students s1 ... s5
members = [t1, s1, s2, s3, s4, s5]
sumgrades = 0
for member in members:
    memberType = member.detail()
    try:
        sumgrades += member.grades
    except AttributeError:
        pass # this would be a teacher, has no grades so skip

print(f"\n{t1.name}'s students have class-average grade = {(sumgrades/5):.1f}")

print('-'*60)

""" result...
Name: Dr. Schard    Age:40 Teaches course: Beginning Python 101
Name: Abigale Agat  Age:20 Average grades: 92
Name: Bertha Belch  Age:22 Average grades: 65
Name: Karl Kuss     Age:21 Average grades: 98
Name: Tom Tippit    Age:22 Average grades: 77
Name: Stew Pitt     Age:20 Average grades: 88

Dr. Schard's students have class-average grade = 84.0
"""

# some extra testing...
# check inheritance
if issubclass(Teacher, SchoolMember):
    print("Class inheritance test:")
    print("Class Teacher is a subclass of class SchoolMember")

print('-'*60)

# test isinstance(object, class-or-type-or-tuple)
print(f"{vars(s2) = }")
if isinstance(s2, Student):
    print("Class instance test:")
    print("Student s2 is an instance of class Student")

'''
Class inheritance test:
Class Teacher is a subclass of class SchoolMember
------------------------------------------------------------
vars(s2) = {'name': 'Bertha Belch', 'age': 22, 'grades': 65}
Class instance test:
Student s2 is an instance of class Student
'''

