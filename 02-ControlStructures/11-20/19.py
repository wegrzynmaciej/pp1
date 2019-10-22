class NegativeZeroError(Exception):
    """ Błąd gdy N <= 0 """
    pass

try:
    x = int(input('Podaj wartość N: '))
    a = 1
    if x <= 0:
        raise NegativeZeroError
    print('Ciąg arytmetyczny o różnicy 3: ', end='')
    for i in range(1,x+1):
        print(a, end=', ')
        a += 3
except ValueError:
    print('Podana wartość jest nieprawidłowa!')
except NegativeZeroError:
    print('Podana wartość jest ujemna lub zerem!')