# Sign your name:Evan Redenius
# In all the short programs below, do a good job communicating with your end user!

# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
PER=(input("What is your name? "))
print("Hey there" ,PER,)
# 2. Write a program where a user enters a base and height and you print the area of a triangle.
b=int(input("What is the base of the triangle"))
h=int(input("What is the height of the triangle"))
A= (b*h)/2
print("The area is",A)

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
R=int(input("What is the radius of your circle: "))
C=(R*3.14)*2
print("The circumfrince is",C)
# 4. Ask a user for an integer and then print the square root.
import math
i=int(input("What number do you want the square root of:"))
SQ=math.sqrt(i)
print("This is the square root",SQ)
# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.

m = int(input("What is the mass: "))
a = int(input("What is the acceleration: "))
F = m*a
print(F)
print("get it?")
