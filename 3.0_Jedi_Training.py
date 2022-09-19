# Sign your name:________________
# In all the short programs below, do a good job communicating with your end user!
import math

# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.

username= input("hello what is your name:")
print("hello",username,",how are you doing today?")
print()
print("----------------------")
print()
# 2. Write a program where a user enters a base and height and you print the area of a triangle.
base =float(input("what is your base of your triangle?"))
height = float(input("what is the height of your triangle"))

area = base*height/2
print("the area of the triangle was",area,"cm^2")

print()
print("----------------------")
print()
# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
r= float(input("what is the radius of your circle?"))
c= 2*math.pi*r
print("the circumference of your circle is",c,"meter" )

print()
print("----------------------")
print()
# 4. Ask a user for an integer and then print the square root.
num = int(input("enter an integer:"))
squareroot =math.sqrt(num)
print("the squareroot of",num,"is",sq)
print()
print("----------------------")
print()
# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
m = float(input("what is the mass of object in kg?"))
a = float(input("what is the acceleration of the object in m/s^2?"))
print("may the",m*a,"be with you")
print("GET IT YOUR LITTLE CRAP!")
print()
print("----------------------")
print()
