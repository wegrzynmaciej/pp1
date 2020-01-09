from math import pi


class Song():

    def __init__(self, author, title, album, year):
        self.author = author
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        return ('{:10} {}\n'
                '{:10} {}\n'
                '{:10} {}\n'
                '{:10} {}\n').format(
                    'Wykonawca:', self.author,
                    'Utwór:', self.title,
                    'Album:', self.album,
                    'Rok:', self.year
        )


class Student():
    last_number = 100000
    uni = 'UEK Kraków'

    def __init__(self, name, surname, field):
        Student.last_number += 1
        self.album_number = Student.last_number
        self.name = name
        self.surname = surname.upper()
        self.field = field

    def __str__(self):
        return '{} {} ({}), {}, {}'.format(
            self.name,
            self.surname,
            self.album_number,
            self.field,
            Student.uni
        )


class Cellphone():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.silent = False
        self.last_call = None

    def __str__(self):
        return '{} {}, rok wydania {}. Tryb cichy jest {}. {}'.format(
            self.make,
            self.model,
            self.year,
            'włączony' if self.silent == True else 'wyłączony',
            ('Ostatnio wybrany numer to ' +
             str(self.last_call)) if self.last_call is not None else 'Brak ostatnich połączeń.'
        )

    def toggle_silent_mode(self):
        if self.silent == False:
            self.silent = True
            print("Telefon został wyciszony.")
        else:
            self.silent = False
            print("Tryb głośny został przywrócony.")

    def call(self, number):
        print('Dzwonię pod numer {}'.format(number))
        self.last_call = number

    def redial(self):
        print('Dzwonię pod ostatnio wybrany numer {}'.format(self.last_call))


class Book():

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class TraditionalBook(Book):

    def __init__(self, title, author, year, no_of_pages):
        self.no_of_pages = no_of_pages
        super().__init__(title, author, year)

    def __str__(self):
        return 'Książka papierowa - "{}" autorstwa {}, wydana w {} roku. Książka ma {} stron.'.format(
            self.title,
            self.author,
            str(self.year),
            str(self.no_of_pages)
        )


class E_Book(Book):

    def __init__(self, title, author, year, file_name):
        self.file_name = file_name
        super().__init__(title, author, year)

    def __str__(self):
        return 'E-Book - "{}" autorstwa {}, wydana w {} roku. E-book jest zapisany w pliku {}'.format(
            self.title,
            self.author,
            str(self.year),
            self.file_name
        )


class Student_16():

    @staticmethod
    def sort_students(*args):
        print('\nPosortowana lista studentów: ')
        for elem in sorted(list(args), key=lambda Student_16: Student_16.album_number):
            print(elem)

    def __init__(self, name, surname, album_number):
        self.album_number = album_number
        self.name = name
        self.surname = surname

    def __str__(self):
        return '{} {} {}'.format(
            self.name,
            self.surname,
            self.album_number,
        )

    def __repr__(self):
        return repr('{} {} {}'.format(self.name, self.surname, self.album_number))

    def __eq__(self, other):
        if self.album_number == other.album_number:
            return 'Studenci mają ten sam numer albumu.'
        else:
            return 'Studenci mają różne numery albumów.'

    # chyba chodziło o __le__ a nie __lt__? chyba że operator < ?
    def __le__(self, other):
        if self.album_number <= other.album_number:
            return 'Student {} {} ma mniejszy lub równy numer albumu od studenta {} {}'.format(self.name, self.surname, other.name, other.surname)
        else:
            return 'Student {} {} ma wyższy numer albumu od studenta {} {}'.format(self.name, self.surname, other.name, other.surname)


class Area():

    @staticmethod
    def calc_triangle(base, height):
        print('Pole trójkąta o podstawie {} i wysokości {} wynosi {} jednostek kwadratowych.'.format(
            base,
            height,
            (base*height)/2
        ))

    @staticmethod
    def calc_rectangle(a, b):
        print('Pole prostokąta o bokach {} i {} wynosi {} jednostek kwadratowych.'.format(
            a,
            b,
            a*b
        ))

    @staticmethod
    def calc_circle(radius):
        print('Pole koła o promieniu {} wynosi {:.4f} jednostek kwadratowych'.format(
            radius,
            pi * radius**2
        ))


class Vehicle():

    def __init__(self, model, plate):
        self.model = model
        self.plate = plate
        self.mileage = 0
        self.is_rented = False

    def __str__(self):
        return '{} {}\nPrzebieg: {}km\nPojazd aktualnie {}jest wypożyczony.'.format(
            self.model,
            self.plate,
            self.mileage,
            '' if self.is_rented else 'nie '
        )

    def change_mileage(self, new_mileage):
        self.mileage += new_mileage

    def rented(self, status):
        self.is_rented = status


class PassengerCar(Vehicle):

    type = 'osobowy'

    def __init__(self, model, plate, seats):
        self.seats = seats
        super().__init__(model, plate)

    def __str__(self):
        return 'Samochód {}, liczba miejsc {}.\n{}'.format(
            PassengerCar.type,
            self.seats,
            super().__str__()
        )


class Truck(Vehicle):

    type = 'dostawczy'

    def __init__(self, model, plate, capacity):
        self.capacity = capacity
        super().__init__(model, plate)

    def __str__(self):
        return 'Samochód {}, ładowność {} ton.\n{}'.format(
            Truck.type,
            self.capacity,
            super().__str__()
        )


class Rental():

    def __init__(self, name, *list_of_cars):
        self.name = name
        if list_of_cars:
            self.cars = list_of_cars
        else:
            self.cars = []

    def __str__(self):
        arr = []
        for car in self.cars:
            arr.append('{}. {} {} {}, {}km, {} {}'.format(
                self.cars.index(car)+1,
                car.type,
                car.model,
                car.plate,
                car.mileage,
                car.seats if car.type == 'osobowy' else car.capacity,
                'miejsc' if car.type == 'osobowy' else 'ton'
            ))
        return '{}\nLista samochodów:\n{}'.format(
            self.name,
            '\n'.join(elem for elem in arr)
        )

    def add_cars(self, *new_car):
        for car in new_car:
            self.cars.append(car)

    def list_available_cars(self):
        arr = []
        counter = 1
        for car in self.cars:
            if not car.is_rented:
                arr.append('{}. {} {} {}, {}km, {} {}'.format(
                    # jeżeli ta sama numeracja co w liście ogólnej
                    # to odkomentować:
                    # self.cars.index(car)+1,
                    # to zakomentować:
                    counter,
                    car.type,
                    car.model,
                    car.plate,
                    car.mileage,
                    car.seats if car.type == 'osobowy' else car.capacity,
                    'miejsc' if car.type == 'osobowy' else 'ton'
                ))
                counter += 1
        print('\nLista dostępnych samochodów:\n{}'.format(
            '\n'.join(elem for elem in arr)
        ))

    def list_rented_cars(self):
        arr = []
        counter = 1
        for car in self.cars:
            if car.is_rented:
                arr.append('{}. {} {} {}, {} {}'.format(
                    # jeżeli ta sama numeracja co w liście ogólnej
                    # to odkomentować:
                    # self.cars.index(car)+1,
                    # to zakomentować:
                    counter,
                    car.type,
                    car.model,
                    car.plate,
                    car.seats if car.type == 'osobowy' else car.capacity,
                    'miejsc' if car.type == 'osobowy' else 'ton'
                ))
                counter += 1
        print('\nLista wypożyczonych samochodów:\n{}'.format(
            '\n'.join(elem for elem in arr)
        ))

    def rented(self, car_plate, status, *mileage):
        for car in self.cars:
            if car.plate == car_plate:
                car.rented(status)
                if not status:
                    car.change_mileage(
                        int(input('Podaj ilość przejechanych kilometrów: ')) if not mileage else int(*mileage))
