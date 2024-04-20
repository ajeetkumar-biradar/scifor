# Nidhi loves to travel to different countries. She is now in a country where the temperature is measured in Fahrenheit and she is not able to understand it in a better way. To help her in this situation, write program to convert temperature from Fahrenheit to celsius. ● Hint: (0°C × 9/5) + 32 = 32°F

fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

print("Temperature in Celsius:", celsius)