###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
a_side = int(a)
b = input('b=')
b_side = int(b)
c = input('c=')
c_side = int(c)
cuboid_volume = int(a_side * b_side * c_side)
cuboid_surface_area = int(2 * a_side * b_side + 2 * b_side * c_side + 2 * a_side * c_side)
print(f'The volume of a cuboid with sides {a_side},{b_side},{c_side} is ', cuboid_volume)
print(f'The surface area of a cuboid with sides {a_side},{b_side},{c_side} is ', cuboid_surface_area)