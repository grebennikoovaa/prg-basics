a = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

roww = 0
columnn = 0

for row in a:
    a[0+roww][0+columnn] = 1
    columnn = columnn + 1
    roww = roww + 1
    print(row)

