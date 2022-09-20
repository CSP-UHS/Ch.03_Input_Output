# Sign your name:________________
# In all the short programs below, do a good job communicating with your end user!
import math

# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.

username = input("What's your name?")
print("Hello, "+username+". How are you today?")
# response = input(""+username2+"??? Think I'm a fool??? Want to fight bro?")

#
# # 2. Write a program where a user enters a base and height and you print the area of a triangle.

base= float(input("What is the base of your triangle in cm?"))
height = float(input("What is the height of your triangle in cm?"))
area = base*height/2
print("The area of the triangle was ",area,"cm^2")
#
# # 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
r=float(input("What is the radius of your cirlce in meters"))
c = 2*math.pi*r
print("the circumference of your circle is",c," meters")
#
# # 4. Ask a user for an integer and then print the square root.
integer = int(input("What is the number that you want to square?"))
sq = math.sqrt(integer)
print("The squareroot of ",integer," is ",sq,"!")
# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma.
# #    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
m = float(input("What is the mass of the object in kg?"))
a = float(input("What is the acceleration of the object in m/s^2?"))
print("May the ",m*a," Newtons be with you!")
print("GET IT? LOLOLOLOLOLOLOLOLOLOLOL")


