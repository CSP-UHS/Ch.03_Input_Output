# # Sign your name:Anna Legler
# # In all the short programs below, do a good job communicating with your end user!
import math
#
# # 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
name = input("Whats your name? ")
print("Hello "+name+"!")

# # # 2. Write a program where a user enters a base and height and you print the area of a triangle.
base = int(input("What is the base of the Triangle? "))
height = int(input("What is the height of the Triangle? "))
area = int((base * height)/2)
print("The area of the triangle is "+str(area))

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
radius = float(input("What is the radius of the Circle? "))
c = str(2*math.pi*radius)
print("The circumference of the circle is "+c)
print("The area of the circle is "+area)

# 4. Ask a user for an integer and then print the square root.
number = int(input("Type an integer: "))
sqrt = str(math.sqrt(number))
print("The square root of that number is "+sqrt)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
mass = int(input("What is the mass? "))
accel = int(input("What is the acceleration? "))
force = str(mass*accel)
print("The force is "+force)
print("Get it?")


