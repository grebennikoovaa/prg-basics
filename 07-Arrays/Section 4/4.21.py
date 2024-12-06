def check_elem(arr1, arr2):
    if set(arr1).issubset(set(arr2)):
        result = True
    else :
        result = False
    return result

arr1 = [5, 4, 3, 2]
arr2 = [5, 4, 5, 2]
print(check_elem(arr1, arr2))