from random import randint


class Miasto():

    def __init__(self, nazwa, populacja):
        self.nazwa = nazwa
        self.populacja = populacja

    def __str__(self):
        return '{}, {}'.format(self.nazwa, self.populacja)


class Prostokat():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a*self.b + other.a*other.b


class Zbiory():

    @staticmethod
    def iloczyn(a, b):
        return (a & b)

    @staticmethod
    def suma(a, b):
        return (a | b)

    @staticmethod
    def roznica(a, b):
        return (a-b)


class Macierz():

    def __init__(self, m, n):
        self.value = [[randint(0, 9) for _ in range(n)] for _ in range(m)]

    def print(self):
        for row in self.value:
            print('[ ' + ''.join(["{:<3}"]*len(row)).format(*row) + ']')

    def __add__(self, other):
        if len(self.value) == len(other.value) and len(self.value[0]) == len(other.value[0]):
            temp = Macierz(len(self.value), len(self.value[0]))
            r = 0
            for row in self.value:
                e = 0
                for _ in row:
                    temp.value[r][e] = self.value[r][e] + other.value[r][e]
                    e += 1
                r += 1
            return temp
        else:
            return Macierz(0, 0)


if __name__ == "__main__":

    m1 = Macierz(3, 5)
    m2 = Macierz(3, 5)
    m3 = Macierz(5, 3)
    m4 = Macierz(6, 6)
    m5 = Macierz(0, 0)
    m7 = Macierz(3, 2)
    m6 = m1 + m7
    m1.print()
    print()
    m2.print()
    print()
    m6.print()
