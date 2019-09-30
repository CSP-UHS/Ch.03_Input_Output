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

semester grade= float(input("What is your current grade?")
final exam=
exam worth=
sg(1-ew)+tg(ew/=100) ew=ew/100
'''

print()
print("Welcome to Peggy's Grade Calculator")
print()
sg = float(input("What is your semester grade?"))
fe = float(input("What is your final exam grade?"))
ew = float(input("What is your exam worth?"))
ew = ew/100
grade = sg*(1-ew) + fe*(ew)
print()
print("Your final grade is:", grade)



