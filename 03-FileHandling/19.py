tab = []
with open('03-FileHandling/universities_backup.txt', 'r') as file:
    for line in file:
        tab.append(line.strip('"\n'))

tab.sort()
print(tab)
with open('03-FileHandling/universities.txt', 'w') as file:
    for item in tab:
        file.write(item + '\n')
