def slownie(liczba):
    nazwy = ['zero', 'jeden', 'dwa', 'trzy', 'cztery',
             'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć']
    x = str(liczba)
    cyfry = []
    for elem in x:
        cyfry.append(nazwy[int(elem)])

    return ','.join(cyfry)


print(slownie(2542))
