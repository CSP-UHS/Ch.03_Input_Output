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

semester = int(input('Please Enter Semester Grade: '))  #take variables and turn them into integers
final = int(input('Please Enter Final Exam Grade: '))
weight = int(input('Please Enter Final Exam Weight: '))

overall = ((semester*(100-weight))+(final*weight))/100  #calculate

print('\nYour final grade will be '+str(overall)+'%')   #print answer