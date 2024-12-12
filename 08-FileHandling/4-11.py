with open('integers.txt', 'w') as file:
    for i in range(1,101):
        second = i**2
        third = i**3
        file.write(f"{i},{second},{third}\n")
        print(f"{i},{second},{third}")