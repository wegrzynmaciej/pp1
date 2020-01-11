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
