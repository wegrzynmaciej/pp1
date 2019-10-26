def suma(items):
    """ Funkcja wyświetlająca tablicę oraz sumę wartości """

    suma = 0
    try:
        for item in items:
            suma += item

        print(f"Tablica: {items}")
        print(f"Suma wartości: {suma}")
    except (ValueError, TypeError):
        print("Podany argument nie jest tablicą lub elementy nie są liczbami!")


def wystepuje(co, gdzie):
    """ Sprawdza, czy dany element występuje w tablicy """

    for x in gdzie:
        if x == co:
            flag = True
            break
        else:
            flag = False

    if flag:
        print("Rezultat: Podana liczba występuje w tablicy.")
    else:
        print("Rezultat: Podana liczba nie występuje w tablicy.")


def wyswietl(table):
    """ wyświetla cyfry w układzie 3xN """
    n = 0
    for x in table:
        assert int(x), "W tablicy znajdują się elementy nie będące cyframi"
        if n > 0 and n % 3 == 0:
            print()
        print(f'{x} ', end='')
        n += 1
