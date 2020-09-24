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

sem_Grade = int(input("Enter your semester grade:"))
final_Exam = int(input("Enter your score for your final exam:"))
exam_Worth = int(input("Enter the % of your grade the exam is worth:"))
exam_Worth: float = exam_Worth/100
overall_Grade = sem_Grade*(1-exam_Worth)+final_Exam*exam_Worth
print('This is your overall grade:', overall_Grade)