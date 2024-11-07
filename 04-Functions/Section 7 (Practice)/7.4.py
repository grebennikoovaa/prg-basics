import range

number = int(input('A number: '))
boolean = range.number_in_range(number)

if boolean == True:
    boolean = 'yes'
elif boolean == False:
    boolean = 'no'
print(f"Number {number} in the range <2,15>: {boolean}")