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

print("Welcome to my trapezoid program!\nWant an easy way to calculate the area of a trapezoid?")
base_1=int(input("Please enter the first base. "))
base_2=int(input("Please enter the second base. "))
height=int(input("Please enter the height. "))
print("The area of the trapezoid will now be calculated!")
area=(base_1+base_2)*(height/2)
print("The area is",area)