palindrome = input('Enter: ')

def f(palindrome):
    expr = ""
    for i in reversed(palindrome):
        expr += i 

    if palindrome == expr:
        return True
    else: 
        return False
print(f(palindrome))
