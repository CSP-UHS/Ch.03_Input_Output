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

letterGrades = \
    {"A": 93, "A-": 90, "B+": 87, "B": 83, "B-": 80, "C+": 77, "C": 73, "C-": 70, "D+": 67, "D": 63, "D-": 60, "F": 0}

def overallGrade(sem,final,worth) :
    return sem*(1-worth/100) + final*(worth/100)

def toLetterGrade(percent) :
    for i in letterGrades :
        if percent >= letterGrades.get(i) :
            return i


userSemesterGrade = float(input("What is your semester grade? (%)\n"))
userFinalGrade = float(input("What is your final grade? (%)\n"))
userFinalWorth = float(input("How much is your final worth? (%)\n"))

userOverall = overallGrade(userSemesterGrade,userFinalGrade,userFinalWorth)

print("Your final grade is {}% ({})!{}".format(userOverall,toLetterGrade(userOverall),(userOverall < 60) and " You're failing your classes!" or ""))