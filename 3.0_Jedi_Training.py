#Sign your name: Cal Watson


# 1.) Write a program that asks someone for their name and then prints their name to the screen?
name = input("What is your name? ")
print("Hello",name)

# 2. Write a program where a user enters a base and height and you print the area of a triangle.
print("Want an easy way to calculate the area of a triangle?")
base=int(input("What is the base of the triangle? "))
height=int(input("What is the height of the triangle? "))
area=(base*height)/2
print("The area of the triangle is",area)

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
print("Want an easy way to calculate the circumference of a circle?")
radius=int(input("What is the radius of the circle? "))
pi=3.141592653589793
circumference=radius*pi*2
print("The circumference of the circle is ",circumference)

# 4. Ask a user for an integer and then print the square root.
print("Want an easy way to calculate the square root of an integer?")
integer=int(input("Please enter an integer. "))
square_root=integer**(1/2)
print("The square root is ",square_root)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma.
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
print("Would you like to know what the Force is?")
mass=int(input("What is the mass? "))
acceleration=int(input("What is the acceleration? "))
force=mass*acceleration
print("The force is",force)
print("Get it? ")