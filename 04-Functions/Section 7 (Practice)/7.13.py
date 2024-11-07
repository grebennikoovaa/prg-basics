number_1 = int(input('Enter number 1: '))
number_2 = int(input('Enter number 2: '))
operator = input('Enter the operator: ')

def f(number_1, number_2, operator):
    if operator == "+":
        result = number_1 + number_2
    elif operator == "-":
        result = number_1 - number_2
    elif operator == "*":
        result = number_1 * number_2
    elif operator == "**":
        result = number_1 ** number_2
    elif operator == "%":
        result = number_1 % number_2
    return result

print(f(number_1, number_2, operator))

