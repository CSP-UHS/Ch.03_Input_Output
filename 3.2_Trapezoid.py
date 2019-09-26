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

print()
print("Hello, and welcome to Peggy's trapezoid area calculator!")
print()
a = float(input("What is the value of base 1?"))
b = float(input("What is the value of base 2?"))
h = float(input("What is the value of its height?"))

area = 0.5*(a+b)*h

print()
print("The area of your trapezoid is:", area)
