import math
cont = True
while cont:
    try:
        number = float(input('Enter any number: '))
        assert number > 0
        print(f'sqrt({number}) = {math.sqrt(number)}')
        cont = False
    except:
        print('Please enter a valid number greater than 0')
        cont = True
