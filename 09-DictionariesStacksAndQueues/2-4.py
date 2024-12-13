import json

with open('dogs.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    for key in data:
        if key["age"] < 5:
            for keys, value in key.items():
                print(keys,':', value)
            print('-----------')
                