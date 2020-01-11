days = {
    1: 'Poniedziałek',
    2: 'Wtorek',
    3: 'Środa',
    4: 'Czwartek',
    5: 'Piątek',
    6: 'Sobota',
    7: 'Niedziela'
}

day = input('Wprowadź numer dnia: ')
try:
    day = int(day)
except ValueError:
    print('Niepoprawna wartość')
    exit()
assert day in days, 'Numer dnia poza zakresem 1-7'
print(days[day])
