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
base= int(input("What's the base of the trapezoid?"))
base2= int(input("What's the second or other base of the trapezoid?"))
height= int(input("What's the height of the trapezoid"))
area= (base+base2)/2*height
print("The area of your trapezoid is",area,)