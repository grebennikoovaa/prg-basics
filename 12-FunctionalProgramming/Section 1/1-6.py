dist = int(input("Enter distance in km: "))
travel_hours = int(input("Enter number of travel hours: "))
travel_minutes = int(input("Enter number of travel minutes: "))

avg_speed = lambda distance,hours,minutes: distance // (hours + minutes/60)
result = avg_speed(dist, travel_hours, travel_minutes)
print(result)