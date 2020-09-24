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
print("I will code this and I will make it laugh at you if you have an overall of 69. Hopefully.")      #please dont dock me points for this
semgrade=int(input("Give me your semester grade.  "))                                                   #so for the first example thing above
finalexam=int(input("Give me your final exam grade.  "))                                                #how do i get it to stop at 80.9
examworth=int(input("Cool. How much is the exam worth?  "))                                             #instead of having it go on for like 20 digits
examworth=examworth/100                                                                                 #or getting it to stop at 69 instead
overall=(semgrade*(1-examworth))+(finalexam*examworth)                                                  #of 69.0
if overall == 69:                                                                                       #also you should give ryan muetzel and daniel mitchell
    print("Your overall is:",overall,'hahahahahahhahahahahahahaha')                                     #extra points for helping me with the if else statement
else:(print("Your overall is:",overall,"Congrats, unless you're Ryan Muetzel"))                         #please