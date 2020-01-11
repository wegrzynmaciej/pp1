from random import randint


def roll_dice():
    res = randint(1, 6)
    assert res in range(1, 7), 'Błąd rzutu'
    return res


print(roll_dice())
