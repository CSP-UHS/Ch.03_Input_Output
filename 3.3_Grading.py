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
print("Would you like to know how your grades will end up? Look no further than right here!")


sgrade=int(input("What is your Semester Grade?"))
fgrade=int(input("What is your Final Grade?"))
exworth=int(input("What is your Exam worth?"))
exworth/=100

overall=sgrade*(1-exworth)+(fgrade*exworth)

print("Your Overall grade is",overall)