plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char.isalpha():  
        new_char_code = ord(char) + 1
        if char.islower() and new_char_code > ord('z'): 
            new_char_code = ord('a')
        elif char.isupper() and new_char_code > ord('Z'):  
            new_char_code = ord('A')
        new_char = chr(new_char_code)
    else:
        new_char = char  
    encrypted_text += new_char

    
print("Plain text:", plain_text)
print("Encrypted text:", encrypted_text)