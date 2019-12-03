from classes import TV

channels = ['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox']

tv = TV()
tv.show_status()
tv.on()
tv.show_status()
tv.show_channels()
tv.set_channels(channels)
tv.show_channels()
tv.show_status()
tv.off()
