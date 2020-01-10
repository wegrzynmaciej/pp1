import json

with open('08-DataStructures/notowania.json', encoding="utf-8") as file:
    data = json.load(file)

print('\
NBP - kursy walut\n\n\
{:<8}{:<20}{:<10}{:<8}\n\
{} '.format(
    'Symbol', 'Waluta', 'Kupno', 'Sprzedaż',
    '='*46
))


for elem in data[0]['rates']:
    print('{:<8}{:<20}{:<10}{:<8}'.format(
        elem['code'],
        elem['currency'],
        elem['bid'],
        elem['ask']
    ))
