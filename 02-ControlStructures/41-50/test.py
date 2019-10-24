from random import sample

gracze = ['A', 'B', 'C', 'D', 'E', 'F']

blue = sample(gracze,4)
blue.sort()
print(blue)

if set(['A','B']).issubset(blue):
    print('OK')
else:
    print('NOT OK')