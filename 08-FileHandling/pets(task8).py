def read_from_file(name):
    with open('pets.txt') as file:
        content = file.read()
    return content

file_content = read_from_file('pets.py')
total = 0

for line in file_content:
    word_count = len(line.split())
    total += word_count

print(total)