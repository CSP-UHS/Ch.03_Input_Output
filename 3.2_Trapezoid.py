'''
TRAPEZOID PROGRAM
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area.

Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 18
'''
print("On the off chance that this is someone other than Hermon reading this, why?")
baseone=int(input("Give me a base. and not the beatbox kind.  "))
basetwo=int(input("Cool. Now give me another before I pass out from coding.  "))
height=int(input("Thanks. We're making a trapezoid btw, so I need a height. And don't use mine.  "))
area=((baseone+basetwo)/2)*height
print("Here's your area:",area,)