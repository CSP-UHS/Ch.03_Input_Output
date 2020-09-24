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

sem_grade = float(input("Semester Grade: "))
fin_grade = float(input("Final Exam Grade: "))
weight = float(input("Exam Weight: "))
sem_grade = sem_grade*(100-weight)  # Multiplies semester grade by semester weight
fin_grade = fin_grade*weight  # Multiplies final grade by final weight
overall = float(sem_grade+fin_grade)  # Adds semester grade and final grade
overall = overall/100  # Turns the value into tens values
print()
if 93 <= overall:  #
    print("Overall Grade: ",overall," (A)")
if 90 <= overall < 93:
    print("Overall Grade: ",overall," (A-)")
if 83 <= overall < 90:
    print("Overall Grade: ",overall," (B)")
if 80 <= overall < 83:
    print("Overall Grade: ",overall," (B-)")
if 73 <= overall < 80:
    print("Overall Grade: ",overall," (C)")
if 70 <= overall < 73:
    print("Overall Grade: ",overall," (C-)")
if 63 <= overall < 70:
    print("Overall Grade: ",overall," (D)")
if 60 <= overall < 63:
    print("Overall Grade: ",overall," (D-)")
if 60 > overall:
    print("Overall Grade: ",overall," (F)")
