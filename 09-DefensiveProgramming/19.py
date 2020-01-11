try:
    pesel = input('Podaj PESEL: ')
    int(pesel)
    assert len(pesel) == 11, 'Podany numer nie składa się z 11 cyfr'
    print(pesel)
except ValueError:
    print('Wprowadzona wartość nie składa się z samych cyfr')
