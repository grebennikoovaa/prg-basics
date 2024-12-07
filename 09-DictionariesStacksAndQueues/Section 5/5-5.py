paragraph = "cat dog mouse cat rat cat mouse mouse"
dictionary = paragraph.split()
count = {}
for word in dictionary:
    if word in count:
          count[word] += 1
    else :
          count[word] = 1

for word, occurences in count.items():
    print(f"'{word}' appears {occurences} times.")

