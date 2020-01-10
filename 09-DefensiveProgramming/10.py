try:
    file = open('09-DefensiveProgramming/NoEducation.txt', 'r')
except FileNotFoundError:
    print('Plik nie został znaleziony')
except OSError:
    print('Błąd przy otwieraniu pliku')
finally:
    file.close()
