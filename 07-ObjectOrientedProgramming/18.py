from classes import Vehicle, PassengerCar, Truck, Rental


pass1 = PassengerCar('Toyota Yaris', 'KR 12QW34', 5)
pass2 = PassengerCar('Citroen C3', 'KR PP256S', 5)
pass3 = PassengerCar('Lamborghini Egoista', 'K0 LOLPOOR', 1)
truck1 = Truck('Ford Transit', 'KR 11KF4K', 1.6)
truck2 = Truck('Peugeot Boxer', 'KR ND39F', 1.3)
rental = Rental('RentPol', pass1, pass2)
rental.add_cars(pass3)
print(rental)
rental.rented('M0 LOLPOOR', True)
rental.rented('KR 11KF4K', True)
rental.list_rented_cars()
rental.list_available_cars()
rental.rented('K0 LOLPOOR', False, 950)
rental.list_rented_cars()
rental.list_available_cars()
