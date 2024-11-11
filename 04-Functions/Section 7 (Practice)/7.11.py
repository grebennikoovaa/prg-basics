def f(n):
    if n < 0:
          print("Incorrect input")
     
    elif n > 0 :
          result = "*/" * (n-1) + "*"
     
    else : 
          result = ""
    return result

if __name__ == "__main__":
      print(f(4))
      print(f(1))