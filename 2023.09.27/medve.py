db = 0
for i in range(1, 8):
    print(f'{i}. nap:')
    reggel = float(input('Reggel: '))
    delben = float(input('Délben: '))
    este   = float(input('Este: '))

    atlag = (reggel + delben + este) / 3

    if atlag > 10:
        db += 1

    print()

print(f'A héten {db} nap volt látható a medve.')


