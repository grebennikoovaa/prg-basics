n = int(input('Enter a number: '))

def factorial(n):
    # 0! = 1, 1! = 1
    if n == 0 or n == 1:
        return 1

    # n! = n * (n-1)!
    if n > 1:
        return n * factorial(n-1)

# Calculate factorial of 5
result = factorial(n)
print(f"The factorial of {n} is: {result}")