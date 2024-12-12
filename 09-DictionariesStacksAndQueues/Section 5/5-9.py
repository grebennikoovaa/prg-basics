province_letters = {}
with open ('province.csv', 'r') as file:
    content = file.read()
    for row in content:
        province, letter = row
        province_letters[letter] = province

vehicle_count = 0
for province in province_letters.values():
    vehicle_count += province

with open('vehicle.txt', 'r') as file:
    content = file.read()