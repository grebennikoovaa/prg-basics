def f(d):
    list = set()
    for car, action in d:
        if action == "in":
            list.add(car)
        elif action == "out":
            list.discard(car)
    return sorted(list)

cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]
print(f(cars))
cars1 = [["KR234","in"],["KR234","out"]]
print(f(cars1))