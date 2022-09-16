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

print("Hey I know you suck at your classes but everything will be ok. Let's take a look at your grades.")
semGrade = float(input("What is your grade for this semester?"))
finExam = float(input("What did you get on your final exam?"))
examWorth = float(input("How much was the final worth?"))
overall = (finExam*(examWorth/100))+(semGrade*((100-examWorth)/100))

print("Your final grade for the year is" ,overall,"%. Good Job")