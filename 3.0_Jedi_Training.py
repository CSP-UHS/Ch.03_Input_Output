# Sign your name: Jaxson Maass
# In all the short programs below, do a good job communicating with your end user!

# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
user_name = str(input("Enter your name: "))
print("Hello there",user_name)

# 2. Write a program where a user enters a base and height and you print the area of a triangle.
tri_height = float(input("Enter triangle height: "))
tri_base = float(input("Enter triangle base: "))
bh = 0.5*(tri_height*tri_base)
print("Triangle area : ", bh)

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
radius = int(input("Enter radius here: "))
circum = 2*3.14*(radius)
print("Circumference: ", circum)





# 4. Ask a user for an integer and then print the square root.
integer = float(input("enter a number here: "))
int_equation = integer**0.5
print("New number: ", int_equation)


# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.

mass = float(input("Enter number here: "))
acceleration = float(input("Enter number here: "))
equation = mass * acceleration
print("May the mass times acceleration be with you!", equation)
print("Get it?")




