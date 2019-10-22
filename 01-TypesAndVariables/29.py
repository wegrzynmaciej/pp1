from random import randint
class NotInRange(Exception):
    """ Poza wartościami 1-6 """
    pass

x = randint(1,6)

try:
    y = int(input('Podaj, ile oczek kostki wyrzucił komputer: '))
    if y not in (1,6):
        raise NotInRange
    print(f'Komputer wyrzucił {x}')
    if y == x:
        flag = True
    else:
        flag = False
    print(f'Zgadłeś: {flag}')
except ValueError:
    print('Podana wartość jest nieprawidłowa!')
except NotInRange:
    print('Wprowadzona wartość nie mieści się w zakresie 1-6')
