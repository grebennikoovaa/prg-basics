def transpose_matrix(m):
    result = []  
    for i in range(len(m[0])):  
        new_row = [] 
        for row in m:  
            new_row.append(row[i])  
        result.append(new_row)  
    return result

m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
res = transpose_matrix(m)
for row in res:
    print(row)