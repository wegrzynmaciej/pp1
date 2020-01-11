try:
    net = float(input("Podaj kwotę netto: "))
except:
    raise TypeError('Kwota powinna być liczbą!')
if net <= 0:
    raise ValueError('Kwota mniejsza od zera!')
else:
    gross = float(net)*1.23
    print('Kwota brutto: {:.2f}zł'.format(gross))
