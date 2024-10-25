###
# Program that asks the user for their age and then checks which age group they belong to
#

user_age = int(input('Enter your age: '))

if user_age >= 65:
    print("Senior group")
elif user_age >= 20:
    print("Adult group")
elif user_age >=13:
    print("Teen group")
elif user_age > 0:
    print("Child group")