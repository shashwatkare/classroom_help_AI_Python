# User input

# name = input("What is your name? ")
# print(f"Hello {name}")

# age = int(input("What is your age? "))
# # print(f"You are {age} years old")
# real_age = 10+age
# print(real_age)


# # Exception handling
#

# try:
#     age = int(input("What is your age? "))
#     real_age = 10+age
#     print(real_age)
# except ValueError as e:
#     print("Please enter a valid number")
#     raise e
# except KeyboardInterrupt as e:
#     raise e
# except Exception as e:
#     pass

# try:
#     pass
#     # some code
# except ValueError:
#     pass
#     # some code
# except KeyboardInterrupt:
#     pass

# No module found error
# PYTHONPATH=. python3 session_4_code.py
# Reading and Writing files
# text_file = open("data/text_file.txt", "r")  # r = read, w = write, a = append, a+ = append, r+ = read and write
# # print(text_file.read())
# for line in text_file:
#     if line.startswith("Not"):
#         print(line)
#     print("fin")

# writing to a file
# text_file = open("data/text_file.txt", "w")
# text_file.write("Hello World I am a new line")
#
# # multilines
# text_file = open("data/text_file.txt", "w+")
# text_file.writelines(["Hello World I am a new line\n\t", " We are here in together"])
# text_file.writelines("Hello World I am a new line", " We are here in together")
# text_file.close()
#
# # reading a binary file
# binary_file = open("binary_file.bin", "rb")
# binary_file.read()
# binary_file.close()
#
#
# with open("data/text_file.txt", "r") as text_file:
#     for line in text_file:
#         print(line)
#
# with open("data/text_file.txt", "r") as text_file:
#     data = text_file.readlines()
#     # print(f"this is data in line 68 {data}")
#     for line in data:
#         words = line.split()
#         print(words, type(words))
#
# # Importing modules

# import

# import session_3
# from session_3 import add_r
# import pandas as pd  # install it - ways to install it - pip install <pkg_name>
# import numpy as np
# import matplotlib.pyplot as plt

# sol = add_r(1, 22)
# print(sol)


# ## OOPs
#
#
# Objects >> Methods & Attributes
# Class >> Blueprint


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def program(self, program):
#         return f"{self.name} is enrolled in {program}."
#
#     def age_calculator(self):
#         return f"{self.name} is {self.age} years old."
#
#
# new_student = Student(name="John", age="20")
# print(new_student.name)
# print(new_student.program("AI with Python"))
# print(new_student.age_calculator())
#
#
# Set and Get methods with Python Property


# class C:
#     """
#     This class is for getter and setter methods
#     """
#     def __init__(self):
#         self._x = None
#
#     @property
#     def model(self):
#         """I'm the 'x' property."""
#         print("getter of x called")
#         return self._x
#
#     @model.setter
#     def x(self, path):
#         model _file = open(path, "rb")
#         print("setter of x called")
#         self._x = value
#
#     @x.deleter
#     def x(self):
#         print("deleter of x called")
#         del self._x
#
#
# c = C()  # create a new C object or instantiate a class object
# c.x = 'foo'  # setter called
# foo = c.x  # getter called
# del c.x  # deleter called

# print(c.x)
# # x and _x are not the same
#
#
## Inheritance

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()
# #
#


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
#
#

x = Student("Mike", "Olsen", 2022)
x.welcome()
