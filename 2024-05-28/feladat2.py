def number_input(szoveg, maximum = float('inf')):
    szam = 0
    while True:
        try:
            szam = int(input(szoveg))
            if szam <= 0 or szam > maximum:
                raise Exception
        except:
            pass
        else:
            return szam

napok = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

ev1 = number_input("Kérem az első dátum évét: ")
honap1 = number_input("Kérem az első dátum hónapját: ", 12)
nap1 = number_input("Kérem az első dátum napját: ", napok[honap1 - 1])
print()
ev2 = number_input("Kérem az másdodik dátum évét: ")
honap2 = number_input("Kérem az másdodik dátum hónapját: ", 12)
nap2 = number_input("Kérem a másdodik dátum napját: ", napok[honap2 - 1])

def eltelt_napok(ev1, ev2, honap1, honap2, nap1, nap2):
    napok = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    napok1 = ev1 * 365
    for i in range(0, honap1):
        napok1 += napok[i]
    napok += nap1

    napok2 = ev2 * 365
    for i in range(0, honap2):
        napok2 += napok[i]
    napok += nap2

    return abs(napok1 - napok2)
    

print(f"{ev1}.{honap1}.{nap1} és {ev2}.{honap2}.{nap2} között {eltelt_napok(ev1, ev2, honap1, honap2, nap1, nap2)} nap volt!")