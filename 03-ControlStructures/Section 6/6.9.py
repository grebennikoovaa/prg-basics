###
# Program that prints the name entered from the keyboard, provided it is a female name
#

name = input('Enter name: ')
if name[-1].lower() == 'a':
    print(f"{name} -- Polish female name")
else:
    print(f"{name} -- Not a typical Polish female name")