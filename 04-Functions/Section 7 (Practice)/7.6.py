binary_number = input('Enter a binary code: ')

def f(binary_number):
    for char in binary_number:
        if char not in ('0', '1'):
            return False
    return True
print(f(binary_number))