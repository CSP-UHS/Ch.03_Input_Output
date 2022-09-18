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
#example
#62% = 90%
#94% = 10%
#62(.9) + 94(.1)
#Overall grade = grade(grade worth) = Exam(Exam worth)

sem_grade = int(input("please enter your semester grade:"))
final_exam = int(input("please enter your final exam score:"))
exam_worth = int(input("please enter what the exam is worth:"))
grade_worth = 100-exam_worth
overall = (sem_grade*grade_worth*.01)+(final_exam*exam_worth*.01)
print("your overall grade in the class is",overall,"%")