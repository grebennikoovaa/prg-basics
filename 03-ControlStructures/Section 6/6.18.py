###
# Program that determines in which quadrant of the coordinate system the point P(x, y) is located
#
x = int(input("X:"))
y = int(input("Y:"))
        
if x > 0 and y > 0:
    print(f"Point({x},{y}) is in the first quadrant of the coordinate system")
elif x < 0 and y > 0:
    print(f"Point({x},{y}) is in the second quadrant of the coordinate system")
elif x < 0 and y < 0:
    print(f"Point({x},{y}) is in the third quadrant of the coordinate system")
elif x > 0 and y < 0:
    print(f"Point({x},{y}) is in the fourth quadrant of the coordinate system")

    if x == 0 and y == 0:
        print(f"Point({x}and{y}) is on X and Y axis")
    elif x == 0 and y != O:
        print(f"Point({x}and{y}) is on X axis")
    elif x != 0 and y == 0:
        print((f"Point({x}and{y}) is on Y axis"))
    elif x != 0 and y != 0:
        print((f"Point({x}and{y}) is not on only axis")) 