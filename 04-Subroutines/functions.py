def suma(items):
    """ Funkcja wyświetlająca tablicę oraz sumę wartości """

    suma = 0
    try:
        for item in items:
            suma += item
        
        print(f'Tablica: {items}')
        print(f'Suma wartości: {suma}')
    except (ValueError, TypeError):
        print('Podany argument nie jest tablicą lub elementy nie są liczbami!')
