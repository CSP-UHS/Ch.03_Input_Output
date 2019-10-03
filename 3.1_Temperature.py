'''
TEMPERATURE PROGRAM
-------------------
Create a program that asks the user for a temperature in Fahrenheit, and then prints the temperature in Celsius.

Test with the following:

In: 32  Out: 0
In: 212  Out: 100
In: 52  Out: 11.1
In: 25  Out: -3.9
In: -40  Out: -40

'''
print("Welcome to the greatest Farenheit to Celcius Converter known to all humankind!")

temp=int(input("what is the temperature in degrees Farenheit?"))

temperature=(temp-32)*(5/9)
print("The temperature in celsius is", temperature)