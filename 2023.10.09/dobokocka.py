from dobokocka_f import *
from random import randint

penz = 1000
tovabb = 'i'

print(f"Az ön egyenlege {penz} krajcár")

while tovabb == 'i' and penz > 0:
    t = tet(penz)
    v = tipp()
    dobas = randint(1, 6)
    print(f"Dobas {dobas}, ", end='')

    if v == 'a' and dobas <= 2 or v == 'b' and 2 < dobas <= 4 or v == "c" and 4 < dobas <= 6:
        print("Ön nyert!")
        penz += t * 2
    else:
        print("Ön vesztett!")
        penz -= t

    print(f"Az új összege {penz} krajcár.")

    if penz > 0:
        tovabb = input("Folytatja? (i/n): ")