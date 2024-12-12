def identity_matrix(n) : 
    matrix = []
    num = 0
    for i in range(n) : 
        add = [0 for j in range(n)]
        add[num] = 1
        matrix.append(add)
        num += 1 
    return matrix

n = 3
result = identity_matrix(n)
for row in result:
    print(row)

n = 5
result = identity_matrix(n)
for row in result:
    print(row)

n = 8
result = identity_matrix(n)
for row in result:
    print(row)