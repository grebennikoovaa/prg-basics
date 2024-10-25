###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter_read = input('Enter a letter: ')
print(f'The letter is {letter_read}')

string_number = "20303"
number = int(string_number)
print(f'The number is {number} ')

decimal_number = 304
binary_number = bin(decimal_number)
print(f'304 in binary system is {binary_number}')

decimal_number = 304
hexadecimal_number = hex(decimal_number)
print(f'304 in hexadecimal system is {hexadecimal_number}')

string = "€"
print(ord(string))

result = abs(-17)
print(result)