'''
TEMPERATURE PROGRAM
-------------------
Create a program that asks the user for a temperature in Fahrenheit, and then prints the temperature in Celsius.

Test with the following:

In: 32  Out: 0
In: 212  Out: 100
In: 52  Out: 11.1
In: 25  Out: -3.9
In: -40  Out: ??? Please tell me what this output is! (output is -40)

'''

f0=float(input("what is the temperature in fahrenheit? "))
c0=(5/9)*(f0-32)
print(c0)

