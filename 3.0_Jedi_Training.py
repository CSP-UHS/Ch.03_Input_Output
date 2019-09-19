#Sign your name: Tristan


# 1.) Write a program that asks someone for their name and then prints their name to the screen?
n = str(input("What is your name?"))
print("Hello, ",n,"!")

# 2. Write a a program where a user enters a base and height and you print the area of a triangle.
b = int(input("What is the base? "))
h = int(input("What is the height? "))
a = 0.5*b*h
print("The area is: ",a,"!")

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
r = int(input("What is the radius? "))
c = r*6.28
print("The circumference is: ",c,"!")

# 4. Ask a user for an integer and then print the square root.
x = int(input("What number do you wish to square root? "))
s = x**0.5
print("The square root is: ",s,"!")

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
m = int(input("What is the mass? "))
a = int(input("What is the acceleration? "))
f = m*a
print("May the",f,"be with you!")
print("Get it?")



