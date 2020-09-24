# Sign your name:________________
# In all the short programs below, do a good job communicating with your end user!


# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
username = input("Please enter your name: ")
print("Hello" ,username,end=' ')

# 2. Write a program where a user enters a base and height and you print the area of a triangle.
height = int(input("Enter the height: "))
base = int(input("Enter the base: "))
area = height*base
print("Your area is:" ,area,end='')

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
radius = int(input("Enter the radius: "))
circumference = radius*3.14*2
print("Your circumference is:" ,circumference,end='')

# 4. Ask a user for an integer and then print the square root.
number = int(input("Enter your number: "))
sqrt = number**.5
print("Your square root is:" ,sqrt,end='')

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
mass = int(input("Enter your mass: "))
acceleration = int(input("Enter your acceleration: "))
print("the Force")
print("Get it?")


