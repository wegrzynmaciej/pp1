import json

with open('08-DataStructures/film.json') as file:
    data = json.load(file)

for k, v in data.items():
    print(k, ":", v)
