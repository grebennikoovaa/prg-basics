import re

def f(mnumbers):
    count = 0
    for i in mnumbers:
        if re.match(r"^[+-]?[1-7a-dA-D]+$", i):
            count += 1
    return count
    

print(f(["A15","-31","7abC","+D1","-gH"]))