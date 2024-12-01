number = 23
array = [15, 38, 7, 23, 14]

def occurs(number, array):
    for i in array:
        if number == i:
            return True
    return False

result = (number, array)

if result:
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} does not appear in the array")


