#Sign your name:________________


# 1.) Write a program that asks someone for their name and then prints their name to the screen?
firstname = input("What is your first name?")
lastname = input("What is your last name?")
print("Nice to meet you,",firstname,lastname)

# 2. Write a a program where a user enters a base and height and you print the area of a triangle.
length=int(input("What is the base of the triangle"))
width=int(input("What is the height of the triangle"))
area=(length*width)/2
print("The area of the triangle is",area)

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
radius=int(input("What is the radius of the circle?"))
circumference=radius*2*3.14
print("The circumference of the circle is",circumference)

# 4. Ask a user for an integer and then print the square root.
number=int(input("What is your chosen number for squaring?"))
number=number**0.5
print("The square root is",number)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
mass=int(input("What is the mass?"))
acceleration=int(input("What is the acceleration?"))
Force=mass*acceleration
print("The force is",Force)
print("May the force be with you, ha get it?")

