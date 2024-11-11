def f(expression):
    sum = 0
    terms = expression.replace('-', '+-').split('+')

    for char in terms:
        if terms:
            sum += int(char)

    return sum

if __name__ == "__main__":
    print(f("2+3"))         
    print(f("3+8+1"))     
    print(f("2+3-4+5-0")) 