'''
TEMPERATURE PROGRAM
-------------------
Create a program that asks the user for a temperature in Fahrenheit, and then prints the temperature in Celsius.

Test with the following:

In: 32  Out: 0
In: 212  Out: 100
In: 52  Out: 11.1
In: 25  Out: -3.9
In: -40  Out: ??? Please tell me what this output is! = -40 silly, everyone knows this

'''

print("\033[1mWelcome to the Hermon \033[1m")
temp=int(input("\033[94mWhat is the temperature in Fahrenheit?"))
print("The temperature is",(temp-32)*(5/9),"degrees in Celcius")


