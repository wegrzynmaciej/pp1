wiek = 243
if type(wiek) != int:
    raise TypeError('Wiek powinien być liczbą całkowitą!')
if wiek <= 0 or wiek > 120:
    raise ValueError('Niepoprawna wartość')
print(f'Masz {wiek} lat')
