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
print("\nThis module will calculate how a given final exam score will impact your semester grade.")
while True:
    sem_gr=int(input("\nCurrent semester grade: "))
    exam_gr=int(input("\n-\n\nExpected exam grade: "))
    exam_wt=int(input("\nFinal exam weight (percentage of grade): "))/100
    final_gr=float((exam_gr*exam_wt)+(sem_gr*(1-exam_wt)))
    print("\n-\n\nFinal grade: ","{:0.1f}".format(final_gr))
    print("\n-------------------------------------------")