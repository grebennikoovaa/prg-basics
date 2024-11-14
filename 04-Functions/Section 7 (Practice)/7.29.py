def sum(n):
    if n == 1:
        return 1
    elif n <= 0:
        return None
    return  n + sum(n - 1)

if __name__ == "__main__":
    print(sum(10))
