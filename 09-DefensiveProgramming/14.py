class LessThanZeroError(Exception):
    pass


def pole_prostokata(a, b):
    try:
        if a <= 0 or b <= 0:
            raise LessThanZeroError
        else:
            return a*b
    except LessThanZeroError:
        print('Bok mniejszy lub równy 0!')
        exit()


try:
    a = float(input('Podaj a: '))
    b = float(input('Podaj b: '))
    print(pole_prostokata(a, b))
except ValueError:
    print('Podane wartosci nie są liczbami!')
    exit()
