class LessThanOneError(Exception):
    """ Błąd gdy bok <= 0 """
    pass

try:
    a = int(input('Podaj a: '))
    if a <= 0:
        raise LessThanOneError
    b = int(input('Podaj b: '))
    if b <= 0:
        raise LessThanOneError
    if a == 1:
        for x in range(0,b):
            print('*')
    else:
        for x in range(0,a):
            print('*', end='')
        print()
        if b != 1:
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
    print('Bok prostokąta nie może być mniejszy od 1!')