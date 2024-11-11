def f(name):
    acronym = ""
    words = name.split()
    for char in words:
        acronym += char[0].upper()
    return acronym
    
if __name__ == "__main__":
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))