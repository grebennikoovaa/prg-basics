number = int(input('Enter a number: '))
even = input("Enter parameter (y/n):")
if even == "n":
    even == False
elif even == "y":
    even = True

def f(number, even):
    sum = 0
    if even == True:
        for char in number:
            char = int(char)
            if char % 2 ==  0:
                sum += char
    elif even == False:
        for char in number:
            char = int(char)
            if char % 2 != 0:
                sum += char
    return sum

if even == True:
    print("Sum of even digits is ", f(number, even))
elif even == False:
    print("Sum of odd digits is ", f(number, even))