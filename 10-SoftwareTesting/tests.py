import unittest
import classes


class Test2(unittest.TestCase):
    def test_miasto_attrs(self):
        # test klasy Miasto
        # zwraca podane wartości
        m = 'Test City'
        p = 123456
        obj = classes.Miasto(m, p)
        self.assertEqual(obj.nazwa, m)
        self.assertEqual(obj.populacja, p)

    def test_miasto_as_string(self):
        # test klasy Miasto
        # czy print() będzie poprawny
        m = 'Test City'
        p = 123456
        obj = classes.Miasto(m, p)
        expected = 'Test City, 123456'
        self.assertEqual(str(obj), expected)


class Test3(unittest.TestCase):
    def test_prostokat_vals(self):
        # Test klasy Prostokąt
        # czy wartości się poprawnie przypisały
        a = 3
        b = 4
        obj = classes.Prostokat(a, b)
        self.assertEqual((obj.a, obj.b), (a, b))

    def test_prostokat_pola(self):
        # Test klasy Prostokąt
        # czy pola się poprawnie sumują
        a1 = 2
        b1 = 2
        p1 = classes.Prostokat(a1, b1)
        a2 = 3
        b2 = 5
        p2 = classes.Prostokat(a2, b2)
        self.assertEqual(p1+p2, 19)


class Test4(unittest.TestCase):
    def test_zbiory_iloczyn(self):
        # Test klasy Zbiory
        # czy iloczyn działa poprawnie
        a = {1, 2, 3, 4}
        b = {2, 4, 6, 8}
        iloczyn = classes.Zbiory.iloczyn(a, b)

        self.assertEqual(iloczyn, {2, 4})

    def test_zbiory_roznica(self):
        # Test klasy Zbiory
        # czy różnica działa poprawnie
        a = {1, 2, 3, 4}
        b = {2, 4, 6, 8}
        roznica = classes.Zbiory.roznica(a, b)
        self.assertEqual(roznica, {1, 3})


class Test6(unittest.TestCase):
    def test_create_matrix_m_n(self):
        # Test klasy Macierz
        # Czy tworzona macierz jest o podanych wymiarach MxN
        m = 7
        n = 9
        matrix = classes.Macierz(m, n)
        self.assertEqual(len(matrix.value), m)
        self.assertEqual(len(matrix.value[0]), n)

    def test_add_matrixes(self):
        # Test klasy Macierz
        # Czy dodawanie macierzy zwraca poprawne wyniki
        m = 7
        n = 9
        matrix1 = classes.Macierz(m, n)
        matrix2 = classes.Macierz(m, n)
        matrix_sum_success = matrix1 + matrix2
        r = 0
        for row in matrix1.value:
            e = 0
            for _ in row:
                self.assertEqual(
                    matrix1.value[r][e]+matrix2.value[r][e], matrix_sum_success.value[r][e])
                e += 1
            r += 1
        # Macierze różnych wymiarów
        m = 3
        n = 5
        matrix3 = classes.Macierz(m, n)
        matrix_sum_failure_full = matrix1 + matrix3
        self.assertEqual(matrix_sum_failure_full.value, [])
        # M takie samo, N różne
        m = 7
        n = 5
        matrix3 = classes.Macierz(m, n)
        matrix_sum_failure_on_n = matrix1 + matrix3
        self.assertEqual(matrix_sum_failure_on_n.value, [])
        # M różne, N takie samo
        m = 3
        n = 9
        matrix3 = classes.Macierz(m, n)
        matrix_sum_failure_on_m = matrix1 + matrix3
        self.assertEqual(matrix_sum_failure_on_m.value, [])


class Test7(unittest.TestCase):

    def test_stos_wstaw_zdejmij(self):
        # Test klasy Stos
        s = classes.Stos()
        s.wstaw('as')
        s.wstaw(10)
        result = s.zdejmij()
        self.assertEqual(result, '10')

    def test_stos_jest_pusty(self):
        s = classes.Stos()
        result = []
        result.append(s.jest_pusty())
        s.wstaw('as')
        result.append(s.jest_pusty())
        s.zdejmij()
        result.append(s.jest_pusty())
        self.assertEqual(result, [True, False, True])


if __name__ == "__main__":
    unittest.main(verbosity=2)
