players_result = [(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]

def calculate(score):
    result = sum(score) - max(score) - min(score)
    return result

final = list(map(calculate, players_result))
print(final)