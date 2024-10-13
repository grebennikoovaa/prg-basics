import random
computer = str(random.randint(1,6))
you = input("Computer's number is : " )
guess = you == computer
print(f'You won: {guess}')