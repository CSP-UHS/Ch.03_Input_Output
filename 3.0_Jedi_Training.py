# Sign your name:Tom Dau
# In all the short programs below, do a good job communicating with your end user!
import math

# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
name=input(("What is your name?  "))                                        # Asks to input name
print("Hello,",name,end=".  Welcome to coding!")                            # Greets _____
print()                                                                     # Leaves a gap between greeting and next question
print()                                                                     # I forgot how to do it the other way if there was another way


# 2. Write a program where a user enters a base and height and you print the area of a triangle.
base=int(input("Please type in a length (m) for a triangle: "))             # asks for triangle base
height=int(input("Please type in a height (m) for a triangle: "))           # asks for triangle height
area=base*height/2                                                          # calculates the area
print("The area of your triangle is:",area,"m2")                            # answer
print()
print()


# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
radius=int(input("Now, please type in a radius (m) for a circle:  "))       #asks for radius of a circle
circumference=radius*2*3.14                                                 #hooray more calculations
print("The circumference of your circle is:",circumference,"m")             #spits your answer at you
print()
print()


# 4. Ask a user for an integer and then print the square root.
integer=int(input("Please type in a number for me to square root so I can show Hermon I did this:  "))  #i dont wanna explain anymore
squareroot=math.sqrt(integer)                                                                           #i had to import math for this i better be doing it right
print("The square root for the number you chose is:", squareroot)                                       #your answer is in the pile of vomit over there
print()
print()


# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
mass=int(input("One last equation, and then I will stop bothering you.  Please enter a number for the mass:  "))    # I
acceleration=int(input("Now, please enter a number for the acceleration:  "))                                       #Regret
force=mass*acceleration                                                                                             #Every
print("May the force (",force,") be with you!")                                                                     #thing
print("Why does Hermon make us suffer like this I'm so sorry")                                                      #here