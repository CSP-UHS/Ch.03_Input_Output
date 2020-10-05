'''
Grading PROGRAM
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
examgrade=float(input("What is your Final exam grade?"))
examworth=float(input("How much is the Final worth?"))
semgrade=float(input("What is your Semester grade?"))
examworth=examworth/100
examworthe=1-examworth
examgrade=examgrade*examworth
semgrade=semgrade*examworthe
overall=examgrade+semgrade
print()
print("Here's your overall grade:")
print(overall)