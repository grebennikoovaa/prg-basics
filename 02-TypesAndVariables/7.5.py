car_number = input('Enter car registration number')
is_krakow = car_number[0:2] == "KR" or "KK"
print(f'Car is from Krakow: {is_krakow}')