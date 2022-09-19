'''
TEMPERATURE PROGRAM
-------------------
Create a program that asks the user for a temperature in Fahrenheit, and then prints the temperature in Celsius.

Test with the following:

In: 32  Out: 0
In: 212  Out: 100
In: 52  Out: 11.1
In: 25  Out: -3.9
In:-40  Out: -40 Please tell me what the output is???

'''

tempF = float(input("What is the temperature in Farenheit"))
tempC = (tempF-32)*5/9
if tempC<=5:
    print("dang",tempC,"degrees Celsius might want to put on a jacket")
elif 5<tempC<33:
    print(tempC,"degrees Celsius that's pretty nice wheather enjoy your day :)")
elif tempC>=33:
    print("Wow",tempC,"degrees Celsius that's getting pretty hot might want to were light clothes")
else:
    print("That's not a number")

