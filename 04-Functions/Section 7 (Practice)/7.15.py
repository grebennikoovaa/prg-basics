def f(n):
    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    print(f(5))
    print(f(9))
