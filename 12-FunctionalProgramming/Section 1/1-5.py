dist = int(input("Enter distance in km: "))
travel_hours = int(input("Enter number of travel hours: "))
travel_minutes = int(input("Enter number of travel minutes: "))

def avg_speed(distance,hours,minutes):
    time = hours + minutes / 60
    average_speed = distance // time
    return average_speed

result = avg_speed(dist, travel_hours, travel_minutes)
print(result)
