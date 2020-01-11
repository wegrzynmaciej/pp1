def iloczyn_zbiorów(z1, z2):
    try:
        if type(z1) != set or type(z2) != set:
            raise TypeError('Co najmniej jeden z elementów nie jest zbiorem')
    except TypeError as ex:
        print(ex)
        return False
    print('Zbiór A: {}\nZbiór B: {}\nIloczyn A i B: {}'.format(z1, z2, z1 or z2))


a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
c = 'asd'

iloczyn_zbiorów(a, b)
iloczyn_zbiorów(b, c)
