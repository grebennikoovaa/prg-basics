arr = [2, 3, 2, 5, 8, 1, 9, 8]
uniq = []

for i in arr:
    if arr.count(i) == 1:
        uniq.append(i)
print(*arr)
print(*uniq)

