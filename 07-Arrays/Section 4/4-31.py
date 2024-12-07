arr = [[-38, 19], 
       [5,40],
       [-7,11],
       [29,16]
    ]

max = 0
min = 0
for row in arr:
    for i in row:
        if i > max:
            max = i
        if i < min:
            min = i
print(min, max)