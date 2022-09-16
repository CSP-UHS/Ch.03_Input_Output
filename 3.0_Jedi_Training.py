# Sign your name:Aidan Zimmerman
# In all the short programs below, do a good job communicating with your end user!

import math
# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
name=input("Hello, What is your name:")
print("Nice to meet you",name)

print()
print("---------------------------------------")

# 2. Write a program where a user enters a base and height and you print the area of a triangle.
print("Triangle Calculator")
base=float(input("Enter base:"))
height=float(input("Enter height:"))
print("The area of this triangle is:", base*height/2)

print()
print("---------------------------------------")

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
radius=float(input("What is the radius:"))
print(2*radius*math.pi)

print()
print("---------------------------------------")

# 4. Ask a user for an integer and then print the square root.
num=float(input("Give me a number:"))
print("The squareroot of that number is",math.sqrt(num))

print()
print("---------------------------------------")

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
mass=float(input("What is the mass:"))
acceleration=float(input("What is the acceleration:"))
print("May the",mass*acceleration,"be with you")
print("Get it?")

# print("hello world")
#
# print("2+3")
# print(2+3)
# print("hello world")
#
# print("your new score is",60+9,"pts")
#
# print("I want to print a double quote \" right here")
#
# print("Hello \r World")
#
# print("Hello", end=" Here is the end character ")
# print("World")

#the # is above the 3 on the keyboard
'''
This is a docstring
'''

# command slash = comment eveything out
# tab over
# shift tab goes back
#
# miles_driven = float(input("enter the miles driven:"))
# gallons_used = float(input("enter the gallons used:"))
# mpg = miles_driven/gallons_used
# print(mpg)
