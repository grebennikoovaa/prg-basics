def f(x,y,digit):
    digit = str(digit)
    counter = 0
    for num in range(x,y+1):
        counter += str(num).count(digit)
    return counter

print(f(10, 15, 1))
print(f(23, 45, 4))