name = input('Wprowadź imię: ')
assert len(name) >= 3, 'Długość imienia poniżej 3'
surname = input('Wprowadź nazwisko: ')
assert len(surname) >= 3, 'Długość imienia poniżej 3'

print('{}, {}'.format(name, surname.upper()))
