class NotAGradeError(Exception):
    """ Gdy podana wartość nie mieści się w skali 1-6 """
    pass

oceny = ['niedostateczny', 'mierny', 'dostateczny', 'dobry', 'bardzo dobry', 'celujący']

try:
    x = int(input('Podaj ocenę: '))
    if x <= 0 or x > 6:
        raise NotAGradeError
    print(f'Ocena słownie: {oceny[x-1]}')
except ValueError:
    print('Podana wartość nie jest liczbą!')
except NotAGradeError:
    print('Podana wartość nie jest oceną 1-6!')