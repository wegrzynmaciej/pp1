class Message():
    def __init__(self):
        self.message = ''

    def set_message(self, message):
        self.message = message.capitalize() + ' BYE.'


class SMS(Message):
    def __init__(self, number, message):
        self.number = number
        super().set_message(message)

    def send(self):
        print('Wysyłanie SMS na numer {}\nTreść: {}'.format(
            self.number,
            self.message
        ))


class Email(Message):
    def __init__(self, to_address, from_address, topic, message):
        self.to_address = to_address
        self.from_address = from_address
        self.topic = topic
        super().set_message(message)

    def send(self):
        print('Wysyłanie emaila...\n'
              '{:6} {}\n'
              '{:6} {}\n'
              '{:6} {}\n'
              '{:6} {}\n'.format(
                  'Od:', self.to_address,
                  'Do:', self.from_address,
                  'Temat:', self.topic,
                  'Treść:', self.message
              ))
