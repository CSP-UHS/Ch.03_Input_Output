# Sign your name: Ryan Muetzel
# In all the short programs below, do a good job communicating with your end user!


# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
'''
user_Name = input('Please enter your name: ') #takes user's name
print('Hello '+user_Name+'!')
'''

# 2. Write a program where a user enters a base and height and you print the area of a triangle.
'''
height = float(input('Enter Triangle Height: '))  #takes the height and base inputs
base = float(input('Enter Triangle Base: '))
area = 0.5*height*base                              #calculates area
print('The triangle area is ' + str(area))          #prints area
'''

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
'''
radius = int(input('Enter Radius: '))  #takes input and turns it into a integer
circumference = 2*3.14*radius           #calculates circumference
print('The circumference is ' str(circumference))
'''

# 4. Ask a user for an integer and then print the square root.
'''
import math                                         #inputs library to use square root function
number = math.sqrt(float(input('Enter Number: ')))  #takes input and then square roots it
print('The square root is '+ str(number))
'''

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
'''
print('May the mass times accleration be with you!')        #prints joke haha funny
mass = int(input('Enter mass: '))                           #takes inputs
acceleration = int(input('Enter acceleration: '))           
force = mass*acceleration                                   #calculates force
print('The force is '+str(force)+' Newtons \nGet it?')      #prints final statement
'''
