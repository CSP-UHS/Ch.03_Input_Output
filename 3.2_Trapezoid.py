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
print("Want to know the area of a trapezoid?\n\nPut the figures below to find out the area\n")
bsa=float(input("Base A: "))
bsb=float(input("Base B: "))
hgt=float(input("Height: "))
area=bsa+bsb
area=area/2
area=area*hgt
print("\nThe area of the trapezoid is:",area)