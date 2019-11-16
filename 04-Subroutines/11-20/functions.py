
def rzut(ile=1):
    """ Funkcja symulująca rzut kostką """
    from random import randint

    table = []
    for i in range(0, ile):
        table.append(randint(1, 6))

    return table

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

