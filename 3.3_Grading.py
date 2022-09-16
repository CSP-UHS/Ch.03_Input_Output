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
s = float(input("What is the semester grade?"))
f = float(input("What is the final exam grade?"))
w = float(input("What percentage of your grade was the final exam worth?"))
x = (100-w)*0.01
avg = (s*x)+(f*w*0.01)
print("Your final grade is",avg,".")
#idk how to calculate weighted grades im getting incorrect outputs, could you comment the correct formula to use? thank you

