try:
    net = float(input("Podaj kwotę netto: "))
    if net <= 0:
        raise ValueError('Kwota mniejsza od zera!')
    else:
        gross = float(net)*1.23
        print('Kwota brutto: {:.2f}zł'.format(gross))

except TypeError as ex:
    print(ex)
except ValueError:
    print("Kwota nie jest liczbą")
