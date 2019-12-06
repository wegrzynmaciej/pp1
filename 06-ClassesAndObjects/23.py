from classes import Kontakt, ListaKontaktów

k1 = Kontakt('Kowalski Jan', 'jank@onet.pl', '555234000')
k2 = Kontakt('Borek Patrycja', 'bp@o2.pl', '232000199')
k3 = Kontakt('Maj Piotr', 'maj@google.com', '222999100')
k4 = Kontakt('Adamczyk Anna', 'ada@poczta.pl', '100200300')
lista = ListaKontaktów()
lista.add_contact(k1, k2, k3, k4)
lista.show_list()
