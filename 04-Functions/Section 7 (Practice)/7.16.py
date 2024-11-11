
def f(palindrome):
    expr = ""
    for i in reversed(palindrome):
        expr += i 

    if palindrome == expr:
        return True
    else: 
        return False


if __name__ == "__main__" :
   print(f("radar"))
   print(f("name"))
