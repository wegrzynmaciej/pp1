class Element:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f'{self.value}'


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def remove(self):
        if not self.is_empty():
            element = self.head
            self.head = element.prev
            return element
        return None

    def add(self, element):
        if self.head != None and self.head != self.tail:
            self.tail.prev = element
            element.next = self.tail
            self.tail = element
        elif self.head != None:
            element.next = self.head
            self.head.prev = element
        else:
            self.head = element

        self.tail = element

    def is_empty(self):
        return self.head == None

    def __str__(self):
        queue = ''
        element = self.head
        while element != None:
            queue += str(element)+'\n'
            element = element.prev
        return queue


# utwórz stos
queue = Queue()

# dodaj elementy na stos
print('Dodaję do kolejki')
element = Element(5)
print(element)
queue.add(element)


element = Element("abc")
print(element)
queue.add(element)

element = Element(True)
print(element)
queue.add(element)


print(f'\nZawartość kolejki\n{queue}')

print('Zdejmuję z kolejki')
print(queue.remove())

print(f'\nZawartość kolejki\n{queue}')

print('Dodaję do kolejki')
element = Element(5)
print(element)
queue.add(element)

print(f'\nZawartość kolejki\n{queue}')

print('Zdejmuję z kolejki')
print(queue.remove())

print(f'\nZawartość kolejki\n{queue}')
