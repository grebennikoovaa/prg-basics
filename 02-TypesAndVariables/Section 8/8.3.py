###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.

# Input temperature in degrees Celsius from the user
# Convert degrees Celsius to degrees Kelvin
# Convert Celsius to Fahrenheit

celsius = float(input('Enter temperature in Celsius: '))
kevin = 273.15 + celsius
fahrenheit = (celsius * 9/5) + 32
print(f'Temperature in degrees Kelvin is ', kevin)
print(f'Temperature in degrees Fahrenheit is ', fahrenheit)