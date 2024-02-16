from kutya import Kutya
from os import system

kutyak: list[Kutya] = [
    Kutya("Bodri", "puli"),
    Kutya("Cézár", "saláta"),
    Kutya("Rex", "német juhász"),
    Kutya("Béla", "keverék")
]

def main():
    v = ''
    while v != '0':
        v = menu()
        match v:
            case '1':
                lista()
            case '2':
                uj()
            case '3':
                eladas()
            case '4':
                eves()
            case '5':
                mozgas()

def menu():
    system("cls")
    print("1..Kutyák listája")
    print("2..Új kutya")
    print("3..Kutya eladása")
    print("4..Kutya etetés")
    print("5..Kutya futtatás")
    print("0..Kilépés")
    return input("\nVálasztás: ")

def lista():
    system("cls")
    for k in kutyak:
        print(f"{k.name}: {k.breed}, {k.allapot()}")
    input("\n<Enter>")

def uj():
    system("cls")
    nev = ""
    while nev == "":
        nev = input("A kutya neve: ")

    fajta = ""
    while fajta == "":
        fajta = input("A kutya fajtálya: ")

    kutyak.append(Kutya(nev, fajta))

def eladas():
    k = keres()
    if k != None:
        kutyak.remove(k)
        print("Sikeres eladás")

    input("\n<Enter>")

def eves():
    system("cls")
    k = keres()
    try:
        k.eszik()
        print("A kutya evett")
    except Exception as e:
        print(e)
    input("\n<Enter>")

def mozgas():
    system("cls")
    k = keres()
    try:
        k.mozog()
        print("A kutya mozgott")
    except Exception as e:
        print(e)
    input("\n<Enter>")

def keres() -> Kutya:
    system("cls")
    nev = ""
    while nev == "":
        nev = input("A kutya neve: ")

    i = 0
    while i < len(kutyak) and kutyak[i].name != nev:
        i += 1
    if i < len(kutyak):
        return kutyak[i]

    print("Ilyen nevű kutya nincs a listában.")
    return None

main()