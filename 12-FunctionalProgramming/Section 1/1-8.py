name = input("Name: ")
surname = input("Surname: ")

intials = lambda name, surname: f"{name[0]}{surname[0]}"
result = intials(name, surname)
print(result)