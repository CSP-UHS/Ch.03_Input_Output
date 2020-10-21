import math
# Sign your name: Gerardo Lopez
# In all the short programs below, do a good job communicating with your end user!


# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
name=input("What is your name? ")
print("Hi",name,"!")

# 2. Write a program where a user enters a base and height and you print the area of a triangle.
b=float(input("What is the base of the triangle? "))
h=float(input("What is the height of the triangle? "))
tri=0.5*b*h
print("The area of the triangle is",tri)

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
rad=float(input("What is the radius of the circle? "))
cir=rad*2
print("The circumference of a circle is",cir)

# 4. Ask a user for an integer and then print the square root.
inte=int(input("Type a number "))
inte=math.sqrt(inte)
print(inte)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
ms=float(input("What is the mass of the object? "))
ac=float(input("What is the acceleration of the object? "))
fo=ms*ac
print(fo)
print("Get it?")