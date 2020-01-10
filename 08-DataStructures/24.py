import json
import string
d = dict.fromkeys(string.ascii_lowercase, 0)

with open('08-DataStructures/DontMakeMeWait.txt', 'r') as file:
    data = file.read()

for key in d:
    d[key] = data.count(key)

with open('08-DataStructures/letters_count.json', 'w') as file:
    json.dump(d, file, indent=4)
