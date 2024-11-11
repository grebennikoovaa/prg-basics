import calculations

text = "You never get a second chance to make a first impression"
target_letter = "a"

count = calculations.calculate(text, target_letter)

print(f"The number of letter '{target_letter}': {count}")