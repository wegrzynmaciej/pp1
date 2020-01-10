import json

with open('08-DataStructures/euro.json') as file:
    data = json.load(file)

print('\
NBP - 10 ostatnich notowań EURO\n\n\
{:<14}{:<10}{:<8}\n\
{} '.format(
    'Data', 'Kupno', 'Sprzedaż',
    '='*32
))

for elem in data['rates']:
    print('{:<14}{:<10}{:<8}'.format(
        elem['effectiveDate'],
        elem['bid'],
        elem['ask']
    ))
