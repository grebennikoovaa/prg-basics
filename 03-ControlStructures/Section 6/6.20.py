###
# A program that converts a decimal number into a binaty number
#

dec_number = int(input('Enter decimal number: '))
binary_number = " "

if dec_number == 0:
    binary_number = "0"
else:
    while dec_number > 0:
        remainder = dec_number % 2
        binary_number = str(remainder) + binary_number  # Add remainder at the beginning
        dec_number = dec_number // 2

print(f'{dec_number}(10) = {binary_number}(2)')

