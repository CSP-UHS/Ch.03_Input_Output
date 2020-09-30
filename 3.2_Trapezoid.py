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
def inquire():
    global base1,base2
    base1=int(input("Base 1: "))
    base2=int(input("Base 2: "))
print("\nThis module will calculate the area of a trapezoid.\n")
while True:
    inquire()
    if base1-base2==0:
        print("That's no trapezoid!")
        inquire()
    else:
        height=(int(input("Height: ")))
    area=(base1+base2)*height/2
    if area-int(area)==0:
        print("\nArea: ",int(area),"\n")
    else:
        print("\nArea: ","{:0.1f}".format(area),"\n")