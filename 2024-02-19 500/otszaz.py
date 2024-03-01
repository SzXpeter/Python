from vasarlas import Vasarlas

vasarlasok: list[Vasarlas] = []

def main():
    beolvasas("penztar.txt")
    print(f"2. feladat\nA fizetések száma: {len(vasarlasok)}\n")
    cikkek_szama(2)
    arucikk_adatok()
    darabszam()
    vasarlas_adatai()
    bevetel()

def beolvasas(fajl_nev:str):
    file = open(fajl_nev, 'r', encoding="utf-8")
    kovetkezo_vasarlas: Vasarlas = Vasarlas()
    for sor in file:
        sor = sor.strip()
        if sor == 'F':
            vasarlasok.append(kovetkezo_vasarlas)
            kovetkezo_vasarlas = Vasarlas()
        else:
            kovetkezo_vasarlas.hozzaad(sor)


    file.close()

def cikkek_szama(vasarlo:int):
    print(f"3. feladat\nA(z) {vasarlo}. vásárló {vasarlasok[vasarlo - 1].cikkek_szama()} darab árucikket vásárolt.\n")

def arucikk_adatok():
    arucikk = input("5. feladat\nAdja meg egy árucikk nevét! ")
    elso_index = -1
    utolso_index = -1
    alkalom = 0
    for i in range(len(vasarlasok)):
        if arucikk in vasarlasok[i].arucikkek.keys():
            if elso_index == -1:
                elso_index = i
            utolso_index = i
            alkalom += 1
    
    if alkalom == 0:
        print("Ebből a termékből nem vásároltak.\n")
    else:
        print(f"Az első vásárlás sorszáma: {elso_index + 1}")
        print(f"Az utolsó vásárlás sorszáma: {utolso_index + 1}")
        print(f"{alkalom} vásárlás során vettek belőle.\n")

def darabszam():
    print("6.feladat")
    db = int(input("Adja meg a vásárolt darabszámot! "))
    print(f"{db} darab vételekor fizetendő: {fizetendo_osszeg(db)}\n")

def fizetendo_osszeg(value):
    match value:
        case 1:
            return 500
        case 2:
            return 950
        case _:
            return 400 * value + 150

def vasarlas_adatai():
    print("7. feladat")
    sorszam = 0
    while sorszam < 1 or sorszam > len(vasarlasok):
        sorszam = int(input("Adja meg a vásárlás sorszámát! "))
    for key, value in vasarlasok[sorszam - 1].arucikkek.items():
        print(value, key)

def bevetel():
    file = open("osszeg.txt", 'w', encoding="utf-8")
    for i in range(0, len(vasarlasok)):
        file.write("{0}: {1}\n".format(
            i + 1,
            vasarlasok[i].fizetendo_osszeg()
        ))

    file.close()

main()