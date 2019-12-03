from classes import TV

channels = ['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Puls', 'TV4']

tv = TV()
tv.show_status()
tv.on()
tv.show_status()

for _ in range(12):
    tv.increase_volume()
    tv.show_status()

for _ in range(12):
    tv.decrease_volume()
    tv.show_status()
