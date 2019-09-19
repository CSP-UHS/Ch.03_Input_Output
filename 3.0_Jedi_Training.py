#Sign your name:________________


# 1.) Write a program that asks someone for their name and then prints their name to the screen?
firstname=input("what is your first name?")
print("Hello",firstname)


# 2. Write a a program where a user enters a base and height and you print the area of a triangle.
b = int(input("enter base value"))
h = int(input("enter height value"))
area= (h*b)/2
print("The area is",area)

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
r = int(input("what is the radius"))
circ = r*2*3.14
print("the circumference is",circ)

# 4. Ask a user for an integer and then print the square root.
import math
x = int(input("enter an integer to find the square root"))
square = math.sqrt(x)
print("the square root is",square)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.

m = int(input("enter the mass"))
a = int(input("enter the acceleration"))

yoda = m*a
print("the force is",yoda)
