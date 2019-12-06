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
