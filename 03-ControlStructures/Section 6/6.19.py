###
# Program that prints a survey consisting of three questions
#

question_1 = input('Are you interested in computer science?(y/n): ')
question_2 = input('Do you like playing computer games?(y/n): ')
question_3 = input('Do you have an Instagram account?(y/n): ')

print("\nSURVEY RESULTS")
print(f"Interested in computer science: {'Yes' if question_1 else 'No'}")
print(f"Playing computer games: {'Yes' if not question_2 else 'No'}")
print(f"Has an Instagram account: {'Yes' if question_3 else 'No'}")