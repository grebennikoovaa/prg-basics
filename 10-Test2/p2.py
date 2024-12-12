def f(arr):
    num = arr[0] if arr[0] == arr[1] else arr[1] == arr[2]
    
    for item in arr:
        if item != num:
            print(item)
        
print(f([7, 7, 7, 7, 7, 5, 7]))