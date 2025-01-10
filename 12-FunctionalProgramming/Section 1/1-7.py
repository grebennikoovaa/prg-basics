number = int(input("Enter a num: "))

is_even = lambda number: number % 2 == 0
result = is_even(number)
print(result)