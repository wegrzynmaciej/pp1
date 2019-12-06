from classes import Kostka

k1 = k2 = k3 = Kostka()

for _ in range(7):
    rzuty = [k1.roll_dice(), k2.roll_dice(), k3.roll_dice()]
    print('{:<18}: {}\n'
          '{:<18}: {}\n'.format(
              'Wyrzucone kostki',
              ' '.join(str(x) for x in rzuty),
              'Suma oczek',
              sum(rzuty)
          ))
