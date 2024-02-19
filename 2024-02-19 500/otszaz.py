from vasarlas import Vasarlas

vasarlasok: list[Vasarlas] = []

def main():
    beolvasas("penztar.txt")
    print(f"2. feladat\nA fizetések száma: {len(vasarlasok)}\n")
    cikkek_szama(2)
    print(vasarlasok[1].fizetendo_osszeg())


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


main()