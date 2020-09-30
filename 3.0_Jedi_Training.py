# Sign your name: Joe Schmidt
# In all the short programs below, do a good job communicating with your end user!


# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.

name=input("\nHello there, What is your name?\n\nMy name is: ")
print("Hello there,",name+"!")

# 2. Write a program where a user enters a base and height and you print the area of a triangle.

base=float(input("\nWhat is the length of the base of the triangle?\n"))
height=float(input("\nWhat is the height of the triangle?\n"))
unit=str(input("\nWhat is the unit of these measurements?\n"))
print("\nThe area of the triangle is",base*height/2,unit,"squared")

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.

radius=float(input("What is the radius of the circle?\n"))
unit=str(input("\nIn what unit was the radius measured?\n"))
print("The circumference of the circle is",radius*2/3.14,unit)
print("\n-Note that 3.14 was used in place of pi")

# 4. Ask a user for an integer and then print the square root.

number=int(input("Alrighty, I'm gonna do something funky. Give me a number!\n"))
print(number**2)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.

print("\nAlrighty, I'm gonnna help you calculate force!\n")
mass=int(input("What is the mass of the object in question?  Don't put a unit on it, please.\n"))
unitmass=str(input("\nokay, now give me the unit of mass\n"))
acceleration=int(input("\nOkay, and the acceleration of the object?  Again, no units please.\n"))
unitaccel=str(input("\nAlright, I'll take that unit now\n"))
print("\nThe force of the object is ",mass*acceleration,unitmass+unitaccel+".")

