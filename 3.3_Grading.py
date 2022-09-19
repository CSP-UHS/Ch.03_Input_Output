'''
Grading PROGRAM
---------------
Create a program that asks the user for their semester grade, final exam grade, 
and final exam worth and then calculates the overall final grade. 
Ask your instructor if you don't know how to calculate weighted averages.
You don't have to print out the letter grade. We will do that in the next chapter.
weighted ave: 62% class 94% final, final is worth 10%
1/3(3+5+6) = 1/3(3)+ 1/3(5) + 1/3(6)
62*.90 + 94*.10
Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''
sem = float(input("Enter your semester grade as an integer: "))
final = float(input("Enter your final exam grade as an integer: "))
fw = float(input("Enter your final exam grade weight as a decimal: "))
sw = 1.00-fw
overall = sem*sw+final*fw
print("Your overall grade is",overall,)