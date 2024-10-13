###
# A program that prints your height both in cm and in feet and inches.
#
cm = float(input('Enter your height in cm: '))
feet = cm // 30.48
remainder_cm =  cm % 30.48
inches = remainder_cm // 2.54

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')