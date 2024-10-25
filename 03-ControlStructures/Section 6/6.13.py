###
# Program that prints a message when the specified car speed
#

car_speed = int(input('Enter car speed: '))
speed_limit_min = 40
speed_limit_max = 140

if car_speed >= speed_limit_max:
    print("Warning: invalid car speed!!")
elif car_speed <= 40:
    print("Warning: invalid car speed!!")
else:
    print("Car speed is within the valid range!")
