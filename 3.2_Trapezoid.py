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
x = float(input("What is the first base?"))
y = float(input("What is the second base?"))
z = float(input("What is the height?"))
u = input("What is the unit of measurement?")

a = ((x+y)/2)*z
print("The area is",a,u,"squared.")