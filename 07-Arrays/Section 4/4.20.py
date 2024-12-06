def seperatenum(arr):
    even = []
    for num in arr:
        if num %2 == 0:
            even.append(num)
    print(even)
    odd = []
    for num in arr:
        if num %2 != 0:
            odd.append(num)
    print(odd)
    return even + odd

arr = [7,9,2,4,5,6]
result = seperatenum(arr)
print(result)