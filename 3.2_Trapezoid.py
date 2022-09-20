'''
TRAPEZOID PROGRAM
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area.
'''
Base1 = int(input("What is the first base of your trapezoid?"))
Base2 = int(input("What is the second base of your trapezoid?"))
Height = int(input("What is the height of your trapezoid?"))
area = (((Base1+Base2)/2)*Height)
print("The area of your trapezoid is ",area,"cm^2")
'''
Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 18
'''
