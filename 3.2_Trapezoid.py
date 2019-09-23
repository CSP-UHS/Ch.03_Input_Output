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
Base1=int(input("what is the first base?"))
Base2=int(input("what is the second base?"))
Height=int(input("what is the height of the trapezoid?"))
Area=(Base1+Base2)/2*Height
print("Your area is",Area)