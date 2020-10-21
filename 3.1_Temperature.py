'''
TEMPERATURE PROGRAM
-------------------
Create a program that asks the user for a temperature in Fahrenheit, and then prints the temperature in Celsius.

Test with the following:

In: 32  Out: 0
In: 212  Out: 100
In: 52  Out: 11.1
In: 25  Out: -3.9
In: -40  Out: ??? Please tell me what this output is!

'''

name = input("please input your name:  ")
print("welcome", name, ", to the fahrenheit to celsius calculator")
fahrenheit = float(input("please input your fahrenheit:  "))
celsius = (fahrenheit-32)*5/9
print("your temperature in celsius is", celsius, "degrees celsius")
'''
-40 fahrenheit is -40 celsius
'''