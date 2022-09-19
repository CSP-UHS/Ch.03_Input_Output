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

b_1=float(input("what is the first base of your trapezoid?"))
b_2=float(input("what is the second base of your trapezoid?"))
hght=float(input("what is the height of your trapezoid?"))
trpzd=((b_1+b_2)/2)*hght
print("the area of your trapezoid is",trpzd,"!")

