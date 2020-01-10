a = 2
b = 0
#assert b != 0 and type(a) == int and type(b) == int, 'Złe wartości'
errors = []
if b == 0:
    errors.append('Wartosć b równa 0')
if type(a) != int:
    errors.append(
        'Parametr a jest równy {} : {}, powienien być liczbą całkowitą'.format(a, type(a)))
if type(b) != int:
    errors.append(
        'Parametr b jest równy {} : {}, powienien być liczbą całkowitą'.format(b, type(b)))
assert not errors, "\nWystąpiły błędy:\n{}".format("\n".join(errors))
print(f'{a}/{b} = {a/b}')
