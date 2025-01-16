data = [508,500,512,499,492,511,503,476,501,509]

tolerance = 500 * 0.2

def check(limit):
    return lambda x: x - 500 <= limit

incorrect = list(filter(lambda x: not check(tolerance)(x), data))
incorrect_percentage = (len(incorrect) / len(data)) * 100

print(incorrect_percentage)