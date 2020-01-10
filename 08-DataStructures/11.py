from GBP import GBP

print('{:<14}{:<7}\n{}'.format('Data', 'Kurs', '='*21))
for elem in GBP['rates']:
    print('{:<14}{:<7}'.format(elem['effectiveDate'], elem['mid']))
