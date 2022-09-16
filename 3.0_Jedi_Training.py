# Sign your name:________________
# In all the short programs below, do a good job communicating with your end user!
import math

# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
name = input("What is your name? ")
print("Hello", name,"!")

# 2. Write a program where a user enters a base and height and you print the area of a triangle.
base = float(input("Base of triangle?"))
height = float(input("Height of triangle?"))
unit = input("Unit of measurement?")
area = 1/2*base*height
print("Area of the triangle is ",area,unit,"squared.")
# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
r = float(input("What is the radius of your circle?"))
c = 2*math.pi*r
unit = input("Unit of measurement?")
print("The circumference is ", c,unit)
# 4. Ask a user for an integer and then print the square root.
i = int(input("Integer?"))
print("The square root is",math.sqrt(i))
# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
mass = float(input("What is the mass?"))
acc = float(input("What is the acceleration?"))
print("The force is ", mass*acc)
print("Get it?")

# print testing we did in class
# print("Your score is", 1320+17, "pts")
# print("I want to print a double quote \" right here")
# print("Hello \nWorld") #new line wow! #seems to be a hidden \n at the end if you just print with ""
# print("Hello \rWorld")
# print("Hello", end=" ")
# print("World")

# miles_driven = int(input("how many miles driven: "))
# gallons_used = int(input("how many gallons used: "))
# mpg = miles_driven/gallons_used
# print(mpg)

