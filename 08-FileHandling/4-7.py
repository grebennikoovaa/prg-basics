import re

def num_vowels():
    with open('vowels.txt', 'r') as file:
        content = file.read()
        vowels_pattern = r'[aeiouAEIOU]'  
        pattern = re.findall(vowels_pattern, content)  
        return len(pattern)  

vowel_count = num_vowels()  
print(f"The number of vowels in the entered text is: {vowel_count}")
