# Sign your name: Ethan Huynh
import math
# In all the short programs below, do a good job communicating with your end user!


# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.

nm=input("what is your name?")
print("hello "+nm+" how are you doing today")


print()

# 2. Write a program where a user enters a base and height and you print the area of a triangle.

bs=float(input("what is the base of your triangle in centimeters?"))
ht=float(input("what is the height of your triangle in centimeters"))
area=bs*ht/2
print("the area of the triangle was",area,"cm squared!")
print()

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.

rad=float(input("what is the radius of your circle?"))
circum=2*math.pi*rad
print("the circumference of your circle is",circum,"squared")
print()

# 4. Ask a user for an integer and then print the square root.

num=int(input("enter an integer"))
sqrt=math.sqrt(num)
print("the square root of",num,"is",sqrt)
print()

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.

m=float(input("what is the mass of the object in kg?"))
a=float(input("what is the acceleration in m/s^2"))

print("may the",m*a,"newtons be with you!")
print("GET IT")

