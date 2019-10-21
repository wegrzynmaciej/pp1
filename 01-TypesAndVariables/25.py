number = input("Podaj nr rachunku bankowego: ")
output = ''
temp = ''
try:
    int(number)
except ValueError:
    print("Podaj tylko cyfry!")
else:
    numbers = [int(x) for x in str(number)]
    print(numbers)
    numbers.reverse()
    print(numbers)
    for x in numbers:
        temp += str(x)
        if len(temp)%4 == 0 or (len(temp)%4 == 2 and len(output) == 30):
            output += (str(temp) + ' ')
            temp = ''           
    print(output[::-1])