student = 'Mateusz'
stypendium = 950
assert type(stypendium) in (int, float), 'Stypendium nie jest liczbą'
assert stypendium > 0, 'Stypendium jest mniejsze lub równe 0'
wydatki = 920
assert type(wydatki) in (int, float), 'Wydatki nie są liczbą'
assert wydatki > 0, 'Wydatki są mniejsze lub równe 0'

print('Student: {}'.format(student.upper()))
print('stypendium: {} zł'.format(stypendium))
print('Wydatki: {} zł'.format(wydatki))
print('Oszczędności: {} zł'.format(stypendium-wydatki))
