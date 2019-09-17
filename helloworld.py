print("Hello World")
print("this is me")
print(5+4)
print("5+4")
score = 120
print ("Your score is:", score)
print(" I want to print a double quote \\ right here")

firstname = input("what is your first name?")         # What is your name?
lastname = input("Hey " + firstname + " what is your lastname?")
print("Hello",firstname , lastname )

print(firstname , lastname + " Calculate area of a rectangle")

length = int(input("What is the length of the rectangle "))   # area of a rectangle
width = int(input("what is the width of the rectangle "))
area = length*width
print("The area of the rectangle is ",area)

print("Calculate Circumference of a circle")     # Circle circumference
radius= int(input("what is the radius of the circle?"))
circumference = radius*3.14*2
print("The circumference of the circle is ", circumference)

import math

print("give me an integer and I will tell you the square root")       # Square root
number= int(input("what is the number?"))
squa = math.sqrt(number)
print(squa)

print("calculate force")        #f=ma
mass = int(input("first what is the mass?"))
accele = int(input("Now what is the acceleration?"))
force= mass*accele
print("F=",force)
