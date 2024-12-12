import re

def four_char():
    with open('files.txt', 'r') as file:
        content = file.readlines()  
        char_pattern = r'\.[a-zA-Z]{4}$' 
        for data in content:
            data = data.strip()  
            if re.search(char_pattern, data):  
                print(data)

four_char()
