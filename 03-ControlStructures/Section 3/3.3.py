###
# Checking if discount is available  
# The discount is available to children under 18,
# or people 65 or older.
#
age = int(input('Enter your age: '))

if age < 18 or age > 65 :
    print('The discount is available')
else:
    print('The discount is not available for you')