# Sign your name:Matthew Fletcher
# In all the short programs below, do a good job communicating with your end user!

import math
# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
username = input("Hello, What is your name: ")
print("Hello",username+", How are you doing today?")
print()
print("---------------------------------------------------")
# 2. Write a program where a user enters a base and height and you print the area of a triangle.
base = float(input("What is the base of your triangle in cm? "))
height = float(input("What is the height of your triangle in cm? "))
area = (base*height)/2
print()
print("---------------------------------------------------")
print("The area of the triangle is",area,"cm^2")
# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
r = float(input("What is the radius of your circle in meters? "))
c = 2*math.pi*r
print()
print("---------------------------------------------------")
print("The circumference of the circle is",c,"meters")
# 4. Ask a user for an integer and then print the square root.
num = int(input("Enter an integer: "))
sq = num**.5
print("The square root of",num,"is",sq)
print()
print("---------------------------------------------------")
# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
m = float(input("what is the mass in kg? "))
a = float(input("what is the acceleration in m/s^2? "))
print("May the",m*a,"Newtons be with you")
print("Get it????")
'''
print("Hello World")

print("2+3")
print(2+3)

print("your new score is",1030+10,"pts")

print("I want to print a double quote \"right here\"")

print("Hello \nWorld")
print("Hello \rWorld") #prints over top the same line
#every statement has a hidden \n
print("Hello", end=" ") # replacing \n with a space
print("World")
'''
'''
this is a docstring
'''
# command forward/ commentifys multiple lines of code
# highlight a paragraph and press tab to section it off or press shift tab to undo that indent
#
# int()
#
# miles_driven = float(input("Enter the miles driven:"))
# gallons_used = float(input("Enter the gallons used:"))
# mpg = miles_driven/gallons_used
# print(mpg)