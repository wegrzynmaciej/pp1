class NegativeZeroError(Exception):
    """ Błąd gdy N <= 0 """
    pass


try:
    x = int(input('Podaj wartość N: '))
    if x <= 0:
        raise NegativeZeroError
    print('Ciąg arytmetyczny o różnicy 3: ', end='')
    for i in range(1, 3*(x), 3):
        print(i, end=', ')
except ValueError:
    print('Podana wartość jest nieprawidłowa!')
except NegativeZeroError:
    print('Podana wartość jest ujemna lub zerem!')
