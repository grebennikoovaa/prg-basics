###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
swift = input('Enter a SWIFT code: ')
bank_code = swift[:4]
country_code = swift[4:6]
location_code = swift[-2:]
print(f'Bank Code: {swift}')
print(f'Country Code: {country_code}')
print(f'Location Code: {location_code}')