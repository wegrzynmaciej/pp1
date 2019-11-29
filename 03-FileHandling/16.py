import re

komunikat = 'wtorek -23C, środa -21C, czwartek 25C'
temp = re.findall(r'[-]*\d{2}', komunikat)
srednia = sum([int(x) for x in temp])/3

print('{:.2f}'.format(srednia))
