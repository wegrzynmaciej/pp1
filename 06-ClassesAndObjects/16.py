from classes import Ebook

book = Ebook('To', 'Stephen King', 728)
book.open_book()
book.show_status()
for _ in range(325):
    book.read_next()
book.show_status()
for _ in range(64):
    book.read_previous()
book.show_status()
book.close_book()
book.read_next()
