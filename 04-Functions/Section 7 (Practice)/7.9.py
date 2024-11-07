x = int(input('Enter x: '))
y = int(input('Enter y: '))

def f(x,y):
    sum = 0
    numbers = list(range(x, y + 1))
    for char in numbers:
            char = int(char)
            if char % 2 == 0 and char < 0: 
                sum += 1
    return sum

print(f"Sum of negative even numbers ({x},{y}) is ", f(x, y))

