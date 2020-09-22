# Sign your name: Ryan Mullins
# In all the short programs below, do a good job communicating with your end user!


# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.


# 2. Write a program where a user enters a base and height and you print the area of a triangle.


# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.


# 4. Ask a user for an integer and then print the square root.


# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.

import math
#Asks for name input, then prints the name
name = str(input("Please enter your name: "))
print("Hey there "+ name + ".")
print()

#calculates the area of a triangle given the base and the height
base = float(input("Please enter the base length of your triangle in meters: "))
height = float(input("Please enter the height length of your triangle in meters: "))
(triangle) = base*height
triangle = triangle/2
print("Your triangle has an area of" , triangle , "m^2")

print()

#calculates the area of a circle given the radius
radius = float(input("Now enter the radius of your circle in meters: "))
radius = radius*radius
radius = radius*3.14159265358979323
print("The area of your circle is" , radius , "m^2")

print()

#calculates the square root given an integer
integer = int(input("Now type in any integer: "))
square = math.sqrt(integer)
print("The square root of" , integer , "is" , square)

print()

#calculates f=ma
mass = float(input("Now enter in the mass of your object in kg: "))
acc = float(input("Now enter in the acceleration of your location in m/s^2 (9.81 on Earth): "))
force = mass*acc
print("The force of your object is", force , "N")
print()
print("May the mass*acceleration be with you, get it?")