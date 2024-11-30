arr = [2, 6, 4, 9, 7]

def star(n):
    result = '*' * n
    return result

for num in arr:
    print(f'{num} : {star(num)}')
      