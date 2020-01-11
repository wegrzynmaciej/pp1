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
    def test_zbiory_dzialania(self):
        # Test klasy Zbiory
        # czy działania działają poprawnie
        a = {1, 2, 3, 4}
        b = {2, 4, 6, 8}
        iloczyn = classes.Zbiory.iloczyn(a, b)
        suma = classes.Zbiory.suma(a, b)
        roznica = classes.Zbiory.roznica(a, b)
        self.assertEqual(iloczyn, {2, 4})
        self.assertEqual(suma, {1, 2, 3, 4, 6, 8})
        self.assertEqual(roznica, {1, 3})


if __name__ == "__main__":
    unittest.main()
