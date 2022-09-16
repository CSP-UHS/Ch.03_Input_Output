# Sign your name:Tanner E.
# In all the short programs below, do a good job communicating with your end user!


# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.

name = input("What's your name?")
Greeting = ("Hello, " + name + " nice to meet you")
print(Greeting)

# 2. Write a program where a user enters a base and height and you print the area of a triangle.

base = int(input("What is the base of the triangle?"))
height = int(input("What is the height of the triangle?"))
areaOfTriangle = base*height/2
print("The area of the Triangle is:",areaOfTriangle,"cm^2")

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.

radius = float(input("What is the radius of the circle in meters?"))
circumference = 2*3.14*radius
print("The circumference of your circle is",circumference,"meters")

# 4. Ask a user for an integer and then print the square root.

number = int(input("Give me a number any whole number: "))
root = number**.5
print("The squareroot of",number,"is",root)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.

mass = float(input("What is the mass of the object in kg? "))
acceleration = float(input("What is the acceleration of the object in m/s^2"))
print("May the",mass*acceleration,"Newtons be with you!")
print("GET IT? LOLOLOLOLOL")