# Sign your name: Alex Mears
# In all the short programs below, do a good job communicating with your end user!


# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
name=input("what is your name?")
print("hello",name,"it is nice to meet you!")
# 2. Write a program where a user enters a base and height and you print the area of a triangle.
base=int(input("base of the triangle in m:"))
height=int(input("height of the triangle in m:"))
print((base*height)/2,"m")
# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
rad=int(input("radius of the circle in m:"))
print("the circumference of the circle is ",rad*3.14*2,"m")
# 4. Ask a user for an integer and then print the square root.
sr=int(input("What is a number?"))
print("The square root of that number is",sr**(1/2))
# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
print()
print("May the mass times acceleration be with you!\n")
mass=int(input("Mass of the object:"))
accel=int(input("Acceleration of the object:"))
print("The force of the object is",mass*accel,"Newtons\n")
print("Get it?")



