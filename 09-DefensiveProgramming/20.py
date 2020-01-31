class Pracownik:
    def __init__(self, osoba, staz_pracy, wynagrodzenie):
        assert type(staz_pracy) == int, 'Staż pracy nie jest liczbą'
        assert staz_pracy >= 0, 'Staż pracy nie może być mniejszy od 0'
        assert type(wynagrodzenie) == int, 'Wynagrodzenie nie jest liczbą'
        assert wynagrodzenie >= 0, 'Wynagrodzenie nie może być mniejszy od 0'
        self.osoba = osoba
        self.staz_pracy = staz_pracy
        self.wynagrodzenie = wynagrodzenie

    def dodatek(self):
        if self.staz_pracy > 5:
            procent = self.staz_pracy - 5
            if procent > 20:
                procent = 20
            procent *= 0.01
            dodatek = self.wynagrodzenie * procent
            return round(dodatek, 2)
        else:
            return 0

    def __str__(self):
        return '\
{}\n\
Staż pracy: {} lat\n\
Wynagrodzenie podstawowe: {:.2f} PLN\n\
Dodatek stażowy: {:.2f} PLN\n\
Wynagrodzenie łączne: {:.2f} PLN '.format(
            self.osoba,
            self.staz_pracy,
            self.wynagrodzenie,
            self.dodatek(),
            self.wynagrodzenie + self.dodatek()
        )


p1 = Pracownik('Adam Nowak', 9, 3120)
print(p1)
