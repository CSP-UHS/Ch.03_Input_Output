'''
TRAPEZOID PROGRAM
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area.

Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 18
'''

b1 = float(input("What is base 1 of the trapezoid in inches? "))
b2 = float(input("What is base 2 of the trapezoid in inches? "))
h = float(input("What is height of the trapezoid in inches? "))
a = ((b1+b2)/2)*h
print("The area of that trapezoid is",a,"in")