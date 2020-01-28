def znaki(liczba):
    result = ''
    if type(liczba) != int:
        print("Błędna wartość")
        return False
    elif liczba < 0:
        liczba *= -1
        result += '- '
    for cyfra in str(liczba):
        result += int(cyfra)*'*' + ', '
    print(result)


znaki(-12323)
