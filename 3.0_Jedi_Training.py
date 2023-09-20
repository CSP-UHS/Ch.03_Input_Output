# 3.0 Jedi Training (20pts)  Name:____Jackson Krier_____


# In all the short programs below, do a good job communicating with your end user!
        # okay

# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name. (1pt)

name = input('Name: ')
print("Hello " + name + "!\n")

# 2. Write a program where a user enters a base and height and you print the area of a triangle. (1pt)
print("\u001b[31mCalculating area of a triangle: ")
base = int(input('Enter a base: '))
height = int(input('Enter a height: '))
triangle_area = float((base * height) / 2)
print(triangle_area)
print("\n")

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference. (1pt)
print("\u001b[32mCalculating circumference of a circle: ")
radius = int(input('Enter a radius for a circle: '))
circumference = 2 * 3.14 * radius
print(circumference)
print("\n")

# 4. Ask a user for an integer and then print the square root. (1pt)
print("\u001b[36mCalculating square root: ")
integer = int(input('Enter an integer: '))
sq_root = integer ** .5
print(sq_root)
print("\n")

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma.

#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next. (1pt)

'''
6. TEMPERATURE PROGRAM (5pts)
-------------------
Create a program that asks the user for a temperature in Fahrenheit, and then prints the temperature in Celsius.

Test your program with the following data:

In: 32  Out: 0
In: 212  Out: 100
In: 52  Out: 11.1
In: 25  Out: -3.9
In: -40  Out: ??? Please tell me what this output is!

    -40 degrees fahrenheit is also -40 degrees celcius
'''
print("\u001b[33mTransitioning fahrenheit to celcius: ")
temp = int(input('Enter a temperature in Fahrenheit: '))
f_to_c = (temp-32) * (5/9)
print(f_to_c)
print("\n")
'''
7. TRAPEZOID PROGRAM (5pts)
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area.

Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 18
'''
print("\u001b[35mCalculating the area of a trapezoid: ")
base_one = int(input('Enter the first base: '))
base_two = int(input('Enter the second base: '))
height = int(input('Enter the height: '))
trapezoid_area = ((base_one + base_two) / 2) * height
print(trapezoid_area)
print("\n")

'''
8. GRADING PROGRAM (5pts)
---------------
Create a program that asks the user for their semester grade, final exam grade, 
and final exam worth and then calculates the overall final grade. 
Ask your instructor if you don't know how to calculate weighted averages.
You don't have to print out the letter grade. We will do that in the next chapter.

Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''
print("\u001b[33mCalculating your final grade: ")
sem_grade = int(input("Enter your semester grade: "))
final_exam_grade = int(input("Enter your final exam grade: "))
exam_worth = float(input("What was the exam worth: "))
exam_worth /= 100
overall = (sem_grade * (1 - exam_worth)) + (final_exam_grade * exam_worth)
print(overall)



