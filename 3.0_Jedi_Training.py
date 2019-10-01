# Sign your name: Peggy Barley


# 1.) Write a program that asks someone for their name and then prints their name to the screen?

print()
name = str(input("What is your name?"))
print("Hello,", name,"!")
print()

# 2. Write a a program where a user enters a base and height and you print the area of a triangle.

print()
print("Welcome to the triangle area calculator!")
base = float(input("What is the base of your triangle?"))
height = float(input("What is the height o your triangle?"))
area = 0.5*(base*height)
print()
print("The area of your triangle is", area)
print()

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.

print()
print ("Welcome to the circumference calculator!")
r = float(input("What is the radius of your circle?"))
cir = 3.14*(r*2)
print()
print("The circumference of your circle is", r)
print()

# 4. Ask a user for an integer and then print the square root.

print()
print ("Welcome to the square root calculator!")
inte = int(input("Type an integer!"))
sr = inte**0.5
print()
print("The square root of", inte, "is", sr)
print()

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.

print()
print("Welcome to the force calculator!")
m = float(input("What is the mass?"))
a = float(input("what is the acceleration?"))
f = m*a
print()
print("The force is", f)
print("May the mass times acceleration be with you!")
print("Get it?")
print()