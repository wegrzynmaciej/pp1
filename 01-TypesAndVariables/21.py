# Celsjusz na Kelvin

try:
    x = int(input('Podaj temperaturę w C: '))
    print(f'{x}C to {float(x)+273.15}')
except ValueError:
    print('Podana wartość nie jest liczbą!')
