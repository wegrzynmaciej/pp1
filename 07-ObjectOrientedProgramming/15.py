from classes import Book, E_Book, TraditionalBook

b1 = E_Book('Miecz przeznaczenia', 'Andrzej Sapkowski',
            1992, 'A_Sapkowski_Miecz_Przeznaczenia.pdf')
b2 = TraditionalBook('Ja, Inkwizytor. Kościany Galeon',
                     'Jacek Piekara', 2015, 402)
print(b1)
print(b2)
