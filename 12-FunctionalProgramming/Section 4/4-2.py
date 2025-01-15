recorded_values = [48,47,54,50,42,68,39,46]

counter = list(filter(lambda speed: speed > 50, recorded_values))
print(f'Speed too high: {counter}')