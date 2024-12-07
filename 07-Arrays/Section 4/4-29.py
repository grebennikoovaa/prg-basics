x = 3
y = 5

def create_2d_arr(x,y):
    arr = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(0)
        arr.append(row)
    return arr

array_2d = create_2d_arr(x, y)
for row in array_2d:
    print(row)