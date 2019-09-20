#Sign your name: Lily Burkhead


# 1.) Write a program that asks someone for their name and then prints their name to the screen?
name=input("What is your name?")
print(("Hello",name))

# 2. Write a a program where a user enters a base and height and you print the area of a triangle.
print("Finding the area of a triangle")
base=int(input("What is the base of the triangle?"))
height=int(input("What is the height of the triangle?"))
area=.5*(base*height)
print(area)

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
import math
print("Lets find the circumference of a circle")
radius=int(input("What's the radius of the circle?"))
circumference=radius*2*math.pi
print(circumference)
# 4. Ask a user for an integer and then print the square root.
print("Lets Find the square root of a number")
num=int(input("Enter a number to find its square root."))
squr=int(num**.5)
print(squr)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
print("May the mass times acceleration be with you!")
mass=int(input("What is the mass?"))
acceleration= int(input("What is the acceleration?"))
force=mass*acceleration
print(force)
print("Get it?;)")


