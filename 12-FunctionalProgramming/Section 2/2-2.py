names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']
sorted_list = lambda names: sorted(names, key=len)
result = sorted_list(names)
for i in result:
    print(i)