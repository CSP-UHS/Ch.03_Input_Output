'''
Grading PROGRAM
---------------
Create a program that asks the user for their semester grade, final exam grade, 
and final exam worth and then calculates the overall final grade. 
Ask your instructor if you don't know how to calculate weighted averages.
You don't have to print out the letter grade. We will do that in the next chapter.
'''
sg = int(input("What was your Semester grade?"))
fg = int(input("What was your Final grade?"))
w= int(input("What was your Final Exam worth?"))/100
r = (1-w)
FinalGrade=float((sg*r+fg*w))
print(FinalGrade)

'''

Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''
