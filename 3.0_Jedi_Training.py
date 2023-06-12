# Sign your name:_Shea_
# In all the short programs below, do a good job communicating with your end user!
import math

# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
name = str(input("Enter your Name:"))
print("Hello " + name +"!")
# 2. Write a program where a user enters a base and height and you print the area of a triangle.
base = int(input("Enter a Base:"))
height = int(input("Enter a Height:"))
print("The area of the triangle is:", (base*height)/2)
# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
radius = float(input("Enter a Radius:"))
print("The circumference of the circle is:", 2* math.pi*radius)
# 4. Ask a user for an integer and then print the square root.
integer = int(input("Enter a Integer:"))
print("The square root of your Integer is:", integer**.5)
# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
mass= float(input("Enter a Mass:"))
acceleration= float(input("Enter a Acceleration:"))
print("Your power in the force is:", mass*acceleration)
print("Get it?")