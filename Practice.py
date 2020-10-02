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

print()
print("So you want to know what your grade will be? \nBeen slacking and want to know what you need to get an A?\n")
print("Luckily for you I have been tasked with making a program to tell you")
print("Just fill out the info and I'll tell you what your grade will be", end=("\n\n"))

sg=float(input("Your current grade in %:"))
fe=float(input("The grade you want to get on your final exam in %:"))
ew=float(input("How much your final exam is worth in %:"))
gw=float(100-ew)
fg=(sg*(gw/100))+(fe*(ew/100))
ffg=input("\nyour final grade is",fg,"%")

if fg > 100:
    print("\033[94mUhh, okay showoff")

if 100 >= fg >= 90:
    print("\033[94mThats an A, nice work!")

if 88.99 >= fg >= 80:
    print("\033[92mThats a B, not bad")

if 79.99 >= fg >= 70:
    print("C's get degrees!")

if 69.99 >= fg >= 69.01:
    print("Gonna need to bump that up a little more, its a D")

if fg == 69:
    print("nice lmao")

if 68.99 >= fg >= 60:
    print("Gonna need to bump that up a little more, its a D")

if fg <= 59.99:
    print("You are a failure")