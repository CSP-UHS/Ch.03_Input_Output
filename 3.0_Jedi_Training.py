# Sign your name: Matthew Hammerand
# In all the short programs below, do a good job communicating with your end user!

import math
print("Welcome Mer. Hermon to my amazing chapter 3 Jedi Training!")
# 1. Write a program that asks someone for their name and then prints a greeting that uses their name.
username = input("Hello! What is your name: ")
print("Hello "+username+", how are you doing today?")
print()
print("---------------------------------")
print()
# 2. Write a program where a user enters a base and height and you print the area of a triangle.
base = float(input("What is the base of your triangle in cm? "))

height = float(input("What is the height of your triangle in cm? "))

area = base*height/2
print("The area of the tiangle was",area,"cm^2")
print()
print("---------------------------------")
print()
# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
r = float(input("What is the radius of your circle in meters? "))
c = 2*math.pi*r
print("the circumference of your circle is",c,"meters")

# 4. Ask a user for an integer and then print the square root.
num = int(input("Enter an interger: "))
sqrt = math.sqrt(num)
print("The square root of",num,"is",sqrt)
print()
print("---------------------------------")
print()
# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
m = float(input("What is the mass of the object in kg? "))
a = float(input("What is the acceleration of the object in m/s^2?"))
print("May the",m*a,"Newtons be with you!")
print("Get IT? LOLOLOLOLOLOLOLOLOLOLOL")




# print("Hello World")
#
# print("2+3")
# print(2+3)
# print("Hello World")
#
# print("your new score is", 1030+10,"pts")
#
# print("I want to pring a double quote \" right here")
#
# print("Hello \n World")
#
# print("Hello", end="Here is the end character")
# print("World")
# # the # is above the three on the keyboard
# '''
# this is a docstring
# '''
#
# """
# command / comments everything highlighted out
# """
#
# miles_driven = float(input("Enter the miles driven:"))
# gallons_used = float(input("Enter the gallons used:"))
# mpg = miles_driven/gallons_used
# print(mpg)

