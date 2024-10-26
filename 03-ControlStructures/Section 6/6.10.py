dogage = int(input("Enter the dog's age in human years: "))
if dogage < 0:
    print("Age cannot be negative.")
else:
    if dogage <= 2:
        age = dogage * 10.5
    else:
        age = 2 * 10.5 + (dogage - 2) * 4
    print(f"The dog's age in dog's years is {age} year(s).")