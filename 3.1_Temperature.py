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

print("Hi!\nWelcome to the Conversion Machine\nPlease enter the temperature below in Fahrenheit\n")
fah=float(input("Fahrenheit Temperature: "))
cel=fah-32
cel=cel*5
cel=cel/9
print()
print("The temperature in Celsius is: ",cel)
print()
print("Thanks for visiting the Conversion Machine\n\nPlease Come Again!")

