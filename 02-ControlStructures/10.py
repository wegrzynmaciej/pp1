print('Program sprawdza, czy podana liczba jest zarówno dodatnia jak i nieparzysta.\n')
try:
    x = int(input('Podaj liczbę: '))
    if x <= 0 or x % 2 == 0:
        print('Podana liczba nie spełnia warunków')
    else:
        print(f'Podana liczba {x} jest zarówno dodatnia jak i nieparzysta')
        
except ValueError:
    print('Podana wartość nie jest liczbą!')