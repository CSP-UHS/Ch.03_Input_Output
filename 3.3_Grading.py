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
grade = int(input("What is your current grade? "))
exam = int(input("What do you want to get on the exam? "))
examWorth = int(input("How much of your grade is the exam worth? "))
gradeWorth = (100-examWorth)/100
newGrade = round(((grade*gradeWorth)+(exam*(examWorth/100))),1)

print("Your new grade will be "+str(newGrade))