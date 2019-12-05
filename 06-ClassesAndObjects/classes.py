from math import gcd
from random import randint, uniform


class University():

    def __init__(self):
        self.name = 'UEK'
        self.fullname = 'Uniwersystet Ekonomiczny w Krakowie'

    def print_name(self):
        print(self.name)

    def set_name(self, new_name):
        self.name = new_name

    def set_fullname(self, new_name):
        self.fullname = new_name

    def print_fullname(self):
        print(self.fullname)


class TV():

    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

    def on(self):
        self.is_on = True

    def off(self):
        self.is_on = False

    def set_channel(self, new_channel):
        self.channel_no = new_channel

    def set_channels(self, channels_list):
        self.channels = channels_list

    def show_channels(self):
        if len(self.channels) > 0:
            print('LISTA KANAŁÓW TV')
            for ch in self.channels:
                print('{}. {}'.format(self.channels.index(ch)+1, ch))

    def increase_volume(self):
        if self.volume != 10:
            self.volume += 1

    def decrease_volume(self):
        if self.volume != 0:
            self.volume -= 1

    def show_status(self):
        if self.is_on:
            if len(self.channels) >= self.channel_no:
                print('Telewizor jest włączony, kanał {} ({}), głośność {}'.format(
                    self.channel_no,
                    self.channels[self.channel_no-1],
                    self.volume
                ))
            else:
                print('Telewizor jest włączony, kanał {}, głośność {}'.format(
                    self.channel_no,
                    self.volume
                ))
        else:
            print('Telewizor jest wyłączony.')


class Ebook():

    def __init__(self, title: str, author: str, page_no: int):
        self.title = title
        self.author = author
        self.page_no = page_no
        self.is_open = False
        self.current_page = 1

    def show_status(self):
        print('Tytuł: {}\n'
              'Autor: {}\n'
              'Liczba stron: {}\n'
              'Bieżąca strona: {}\n'
              .format(
                  self.title,
                  self.author,
                  self.page_no,
                  self.current_page
              ))

    def open_book(self):
        self.is_open = True

    def close_book(self):
        self.is_open = False

    def read_next(self):
        if self.is_open:
            if self.current_page < self.page_no:
                self.current_page += 1
        else:
            print('Książka jest zamknięta.')

    def read_previous(self):
        if self.is_open:
            if self.current_page > 1:
                self.current_page -= 1
        else:
            print('Książka jest zamknięta.')


class Fraction():

    def __init__(self):
        pass

    def create_fraction(self, licznik: int, mianownik: int):
        if mianownik == 0:
            print('Mianownik nie może być 0')
        else:
            self.licznik = licznik
            self.mianownik = mianownik

    def show_fraction(self):
        print('Ułamek: {}/{}'.format(
            self.licznik,
            self.mianownik
        ))

    def simplify_fraction(self):
        nwd = gcd(self.licznik, self.mianownik)
        if nwd != 1:
            self.licznik //= nwd
            self.mianownik //= nwd


class Kostka():

    def __init__(self):
        pass

    def roll_dice(self):
        return randint(1, 6)


class Rachunek():
    def __init__(self, new_number):
        self.number = str(new_number).replace(' ', '')
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print('Niewystarczająca ilość środków na koncie')
        else:
            self.balance -= amount

    def show_status(self):
        print('Numer konta: {} {} {} {} {} {} {}\n'
              'Saldo: {}zł'.format(
                  self.number[0:2],
                  self.number[2:6],
                  self.number[6:10],
                  self.number[10:14],
                  self.number[14:18],
                  self.number[18:22],
                  self.number[22:26],
                  self.balance
              ))


class Samolot():

    def __init__(self, number):
        self.altitude = 0
        self.in_flight = False
        self.number = number

    def show_status(self):
        print('Tu {}. moja wysokość lotu to {}m'.format(
            self.number, self.altitude))

    def start(self, altitude):
        if altitude not in range(1000, 2001):
            print('Niepoprawna wysokość')
        else:
            self.in_flight = True
            self.altitude = altitude

    def change_altitude(self, altitude):
        if altitude > 11000:
            print('Próbujesz lecieć za wysoko')
        elif altitude < 300:
            print('Probujesz lecieć za nisko')
        else:
            self.altitude = altitude

    def land(self):
        if self.altitude >= 500:
            print('Zbyt duża wysokość dla lądowania. Obniż lot.')
            return False
        else:
            self.altitude = 0
            self.in_flight = False
            print('Lądowanie zakończone')


class Statystyka():

    def __init__(self, *args):
        self.numbers = []
        if args:
            for arg in args:
                self.numbers.append(arg)
            self.numbers.sort()

    def add_number(self):
        num = input('Dodaj liczbę: ')
        converted_num = float(
            num) if '.' in num or 'e' in num.lower() else int(num)
        self.numbers.append(converted_num)
        self.numbers.sort()

    def show_numbers(self):
        print(', '.join(str(x) for x in self.numbers))

    def __get_max(self):
        return max(self.numbers)

    def __get_min(self):
        return min(self.numbers)

    def __get_mean(self):
        return sum(self.numbers)/len(self.numbers)

    def __get_median(self):
        if len(self.numbers) % 2 == 0:
            x1 = self.numbers[int(len(self.numbers) / 2)-1]
            x2 = self.numbers[int(len(self.numbers) / 2)]
            return (x1+x2)/2
        else:
            return self.numbers[int(len(self.numbers)/2)]

    def get_statistic(self):
        print('{:<20} : {}\n'
              '{:<20} : {}\n'
              '{:<20} : {}\n'
              '{:<20} : {}\n'
              .format(
                  'Minimum zbioru', self.__get_min(),
                  'Maximum zbioru', self.__get_max(),
                  'Średnia arytmetyczna', self.__get_mean(),
                  'Mediana zbioru', self.__get_median()
              ))


class Termometr():

    def __init__(self):
        self.temperature = None
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def get_temperature(self):
        if self.is_on == True:
            self.temperature = round(uniform(34.0, 42.0), 1)
        else:
            print('Termometr jest wyłączony.')

    def show_temperature(self):
        if self.is_on == True:
            if int(self.temperature*10) in range(370, 410):
                add_msg = ' (gorączka)'
            elif self.temperature >= 41:
                add_msg = ' (stan zagrożenia życia!)'
            else:
                add_msg = ''

            print('Zmierzona temperatura: {}C{}'.format(
                self.temperature, add_msg
            ))
        else:
            print('Termometr jest wyłączony.')


class Kontakt():

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def show_contact(self):
        print('{:20} {:15} {:9}'.format(
            self.name,
            self.email,
            self.phone
        ))


class ListaKontaktów():

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact, *contacts):
        self.contacts.append(contact)
        if contacts:
            for con in contacts:
                self.contacts.append(con)

    def show_list(self):
        for contact in self.contacts:
            contact.show_contact()
