from classes import Cellphone

phone1 = Cellphone('Xiaomi', 'Redmi Note 7', 2019)
phone2 = Cellphone('Apple', 'iPhone X', 2019)

print(phone1)
print(phone2)
phone1.toggle_silent_mode()
phone1.call(123456789)
phone1.redial()
phone2.toggle_silent_mode()
phone2.call(123456789)
phone2.redial()
print(phone1)
print(phone2)
