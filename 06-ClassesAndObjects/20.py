from classes import Samolot

flight = Samolot('LOT881')
flight.start(1500)
flight.show_status()
flight.change_altitude(8900)
flight.show_status()
flight.change_altitude(200)
flight.show_status()
flight.land()
flight.show_status()


flight.change_altitude(300)
flight.land()
flight.show_status()
