# Sign your name: Owen Earp
# In all the short programs below, do a good job communicating with your end user!

# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
username = input("What is your name: ")
print("Hello, "+username+", how are you doing today?")

# 2. Write a program where a user enters a base and height and you print the area of a triangle.
base = float(input("What is the base of your triangle in cm: "))
height = float(input("What is the height of your triangle in cm: "))
area = base*height/2
print("The area of the triangle is",area,"cm squared")

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
r = float(input("What is the radius of the circle in meters: "))
c = 2*3.14*r
print("The circumference of the circle is",c,"meters")

# 4. Ask a user for an integer and then print the square root.
num = int(input("Enter an integer: "))
sqr = num**0.5
print("The square root of",num,"is",sqr)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
mass = float(input("What is the mass of the object in kg: "))
acc = float(input("What is the acceleration of the object in m/s: "))
print("May the",mass*acc,"be with you!")
print("heheheha")