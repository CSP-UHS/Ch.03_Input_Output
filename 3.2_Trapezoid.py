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

one_base = float(input("Please enter the first base length of the trapezoid in meters: "))
print()
two_base = float(input("Please enter the second base length of the trapezoid in meters: "))
print()
height = float(input("Please enter the height of the trapezoid in meters: "))
area = 0.5*(one_base+two_base)*height
print("The area is",area,"m^2")
