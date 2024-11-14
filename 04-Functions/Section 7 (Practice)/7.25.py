def f(text):
    result = ""
    for char in text:
        result = result + char + "-"
    if result:
        result = result[:-1]
    return result

if __name__ == "__main__":
    print(f("University"))
    print(f("UE"))