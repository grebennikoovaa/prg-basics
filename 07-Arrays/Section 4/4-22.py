import random

def rand_elem(array):
    result = random.choice(array)
    return result

array = [7,9,2,4,5,6,16,13,10,17,22]
for i in range(6):
   print(rand_elem(array))