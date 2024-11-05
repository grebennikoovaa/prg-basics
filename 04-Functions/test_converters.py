import converters

print('### Test converters')
centimeters = 300 
print(f'300 cemeters is {converters.cm_to_inch(3)} cm')
inches = converters.cm_to_inch(centimeters)
print(f'{centimeters} cm is {inches} inches')
