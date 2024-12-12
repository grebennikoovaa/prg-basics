def f(array2D):
    n = len(array2D)
   
    for i in range(n):
        row_sum = sum(array2D[i])
        col_sum = sum(array2D[j][i] for j in range(n))
        
        if row_sum != col_sum:
            return False
        
    return True