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

temperature = float(input("Please enter temperature in Fahrenheit: "))
temperature = temperature-32
temperature = temperature*5/9
if temperature > 0:
    print("Temperature: \033[31m{area} °C".format(area=temperature))  # prints the temperature in a different color
if temperature < 0:
    print("Temperature: \033[34m{area} °C".format(area=temperature))
if temperature == 0:
    print("Temperature: \033[33m{area} °C".format(area=temperature))





