import re

def f(first_letter, last_letter):
    with open('data.txt', 'r') as file:
        content = file.read()
        words = re.findall(r'\b\w+\b', content)

        count = 0
        for word in words:
            if word[0] == first_letter and word[-1] == last_letter:
                count += 1
        return count
    
result = f("w", "d")
print(result)