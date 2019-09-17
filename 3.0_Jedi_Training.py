#Sign your name:Henry Hmar


# 1.) Write a program that asks someone for their name and then prints their name to the screen?
firstname = input("what is your first name?")         # What is your name?
lastname = input("Hey " + firstname + " what is your lastname?")
print("Hello",firstname , lastname )

# 2. Write a a program where a user enters a base and height and you print the area of a triangle.
print("Please do this thing")
length = int(input("What is the length of the rectangle "))   # area of a rectangle
width = int(input("what is the width of the rectangle "))
area = length*width
print("The area of the rectangle is ",area)

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
print("Calculate Circumference of a circle")     # Circle circumference
radius= int(input("what is the radius of the circle?"))
circumference = radius*3.14*2
print("The circumference of the circle is ", circumference)

# 4. Ask a user for an integer and then print the square root.
import math

print("Give me an integer and I will tell you the square root")       # Square root
number= int(input("what is the number?"))
squa = math.sqrt(number)
print(squa)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
print("calculate force")        #f=ma
mass = int(input("first what is the mass?"))
accele = int(input("Now what is the acceleration?"))
force= mass*accele
print("F=",force)


