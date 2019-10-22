class LessThanOneError(Exception):
    """ Błąd gdy bok <= 1 """
    pass

try:
    a = int(input('Podaj a: '))
    if a <= 1:
        raise LessThanOneError
    b = int(input('Podaj b: '))
    if b <= 1:
        raise LessThanOneError

    for x in range(0,a):
        print('*', end='')
    print()
    for x in range(0,b-2):
        print('*', end='')
        for y in range(0,a-2):
            print(' ', end='')
        print('*')
    for x in range(0,a):
        print('*', end='')
        
except ValueError:
    print('Podana wartość jest nieprawidłowa!')
except LessThanOneError:
    print('Bok prostokąta nie może być mniejszy ani równy 1!')