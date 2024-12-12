import re

username = input('Enter a username: ')
password = input('Enter a password: ')

username_pattern = r'^[a-zA-Z0-9_]{6,}$'
password_pattern = r'^[a-zA-Z0-9_]{8,}$'

username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)

if username_pattern and password_match:
    print('Correct username and password')
else : 
    print('Incorrect username of password')