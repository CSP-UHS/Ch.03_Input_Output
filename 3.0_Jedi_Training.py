# Sign your name:Kadin Terronez
# In all the short programs below, do a good job communicating with your end user!
import math

# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
print("Hello, what is your name?")
my_name_is = str(input("enter your name:"))
greeting = "Nice to meet you!,"
a = my_name_is
print(greeting,a)


# 2. Write a program where a user enters a base and height and you print the area of a triangle.a,b=12,6
b = float(input("what is the base of your triangle in cm?:"))
h = float(input("what is the height of your triangle in cm?:"))
area = b*h/2
print("the area of the triangle is",area,"cm^2")

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
print("what is the radius of the circle?")
radius = float(input("enter the radius of you circle in cm?:"))
c = radius*2*3.14
print("the circumference of your circle is ",c,"cm")

# 4. Ask a user for an integer and then print the square root.
print("please enter an integer")
integer = int(input("enter an integer:"))
root = math.sqrt(integer)
print("the square root is",root,"")

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
print("May the mass times the acceleration be with you!")
m = float(input("what is the mass?:"))
a = float(input("what is the acceleration?:"))
f = m*a
print("May the",f," Newtons be with you!")
print("get it?")







