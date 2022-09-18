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

one_base = int(input("What is the base of your trapezoid in cm?:"))
two_base = int(input("What is the second base of your trapezoid in cm?:"))
height = int(input("What is the height of your trapezoid in cm?:"))
area = height*((one_base+two_base)/2)
print("the area of your trapezoid is",area,"cm^2")