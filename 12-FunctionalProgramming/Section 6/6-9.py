measures = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

counter = list(filter(lambda x: measures[x] > 0, measures ))
print(f'Cities with positive temperatures: {counter}')