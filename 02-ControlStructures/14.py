class NegativeError(Exception):
    """ Błąd gdy wiek jest wartością ujemną """
    pass

try:
    wiek = int(input('Podaj wiek psa w ludzkich latach: '))
    if wiek < 0:
        raise NegativeError        
    elif wiek <= 2:
        wiek_p = wiek*10.5
    else:
        wiek_p = 21 + (wiek-2)*4
    print(f'Wiek psa w psich latach to {wiek_p} lata')
except ValueError:
    print('Podana wartość nie jest liczbą!')
except NegativeError:
    print('Wiek nie może być ujemny!')