arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
longest_name = arr[0]

for names in arr:
    if len(names) > len(longest_name):
        longest_name = names
print(longest_name)
    
