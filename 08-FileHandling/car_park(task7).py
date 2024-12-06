def read_from_file(name):
    with open('car_park.txt', 'r') as file:
        content = file.read()
    return content

# reads the entire file
file_content = read_from_file('countries.txt')

# splits the entire file contents into lines
# and stores them in an array
file_lines = file_content.splitlines()
file_lines.sort(reverse=False)

# prints the array
total = 0
for line in file_lines:
   total += 1
   print(total, line)