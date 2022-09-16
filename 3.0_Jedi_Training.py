# Sign your name: Matthew
# In all the short programs below, do a good job communicating with your end user!


# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.

yourName = input("What is your name?\n")
print("Nice to meet you {}!\n".format(yourName))

# 2. Write a program where a user enters a base and height and you print the area of a triangle.

while True :
    try:
        base = float(input("Enter your triangle base:\n"))
        height = float(input("Enter your triangle height:\n"))
        break
    except ValueError:
        print("Invalid inputs! Please try again\n")

print("The area of your triangle is {} units^2!\n".format((base*height)/2))

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.

import math

while True :
    try:
        radius = float(input("Enter your circle radius:\n"))
        break
    except ValueError:
        print("Invalid inputs! Please try again\n")

print("The circumference of your circle is {} units!\n".format(radius*2*math.pi))


# 4. Ask a user for an integer and then print the square root.

while True :
    try:
        number = int(input("Enter your number to be square rooted:\n"))
        break
    except ValueError:
        print("Invalid inputs! Please try again\n")

print("The square root of {} is {}!\n".format(number,math.sqrt(number)))

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.

while True :
    try:
        mass = float(input("Enter your mass (kg):\n"))
        acceleration = float(input("Enter your acceleration (m/s^2):\n"))
        break
    except ValueError:
        print("Invalid inputs! Please try again\n")

print("May the {} be with you!\nGet it?".format(mass*acceleration))
