
def rzut(ile=1):
    """ Funkcja symulująca rzut kostką """
    from random import randint

    table = []
    for i in range(0, ile):
        table.append(randint(1, 6))

    return table
