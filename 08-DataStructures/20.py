import json

pc = {
    'type': 'desktop',
    'broken': False,
    'last-reboot': '2019-04-20',
    'specs': {
        'CPU': '2.7 GHz',
        'GPU': 'integrated',
        'RAM': 8,
        'drive': 'HDD 500GB'
    },
    'purchase_date': 2015
}

with open('08-DataStructures/komputer.json', 'w') as file:
    json.dump(pc, file, indent=4)
