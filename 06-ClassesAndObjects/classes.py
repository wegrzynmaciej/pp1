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
        from math import gcd
        nwd = gcd(self.licznik, self.mianownik)
        if nwd != 1:
            self.licznik //= nwd
            self.mianownik //= nwd
