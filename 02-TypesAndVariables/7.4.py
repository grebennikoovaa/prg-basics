import math
tree_circumference = int(input("Tree circumference: "))
diameter = tree_circumference / math.pi
may_be_cut_down = diameter >= 50
print(f'Tree may be cut down: {may_be_cut_down}')