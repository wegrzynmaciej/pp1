# Zamiana z dziesiętnego na binarny


try:
    d = int(input("Podaj liczbę: "))
except ValueError:
    print("Podana wartość nie jest liczbą całkowitą")
else:
    print(type(d))