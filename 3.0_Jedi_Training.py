# Sign your name:_____Aidan______
# In all the short programs below, do a good job communicating with your end user!
import math

# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
name=str(input("what is your name?"))
print("Hello", name)

# 2. Write a program where a user enters a base and height and you print the area of a triangle.
base=float(input("what is the base?"))
height=float(input("what is the height?"))
area= base*height
print(area)
# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
radius=float(input("what is the radius?"))
circ=(radius*2*math.pi)
print(circ)
# 4. Ask a user for an integer and then print the square root.
Number= float(input("what is the number?"))
root=math.sqrt(Number)
print(root)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
print("May the mass times acceleration be with you!")
mass=float(input("what is the mass?"))
acc=float(input("what is the acceleration"))
force=(mass*acc)
print(force)
print("Get it?")


