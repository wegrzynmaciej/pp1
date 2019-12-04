from classes import Rachunek

acc = Rachunek('12 3456 5555 9090 1111 0000 7722')

acc.show_status()
acc.deposit(25.30)
acc.show_status()
acc.withdraw(31.70)
acc.show_status()
acc.withdraw(14)
acc.show_status()
