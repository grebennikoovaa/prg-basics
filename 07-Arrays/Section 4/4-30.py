arr = [[0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0]
] 

for i in range(1, 6):
    for j in range(1, 6):
        arr[i-1][j-1] = i * j
for row in arr:
    print(row)