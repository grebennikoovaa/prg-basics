###
# Calculates arithmetic mean of two integer numbers
#
def mean(x,y):
   sum = x + y
   return sum // 2

# takes two numbers from keyboard
n1 = int(input("num1: "))
n2 = int(input("num2: "))

# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')