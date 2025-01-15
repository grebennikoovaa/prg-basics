from functools import reduce

numbers = [2,4,6,3,7,5]

even = list(filter(lambda x: x % 2 == 0, numbers))
def sum_of_even(x, y):
    return x + y

result = reduce(sum_of_even, even)
print(result)