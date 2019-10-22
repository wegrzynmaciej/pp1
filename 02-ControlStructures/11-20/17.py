sp = 0
sn = 0
for x in range (1,51):
    if x % 2 == 0:
        sp += x
    else:
        sn += x
print(f'Przedział <1,50>\nSuma liczb parzystych: {sp}\nSuma liczb nieparzystych: {sn}')