import os, random

def informacio(penz: int) -> None:
    os.system("cls")
    print(f"Rulett játék \t\t\t Jelenlegi egyenleg: {penz}$")
    print("\n\n")

def menu() -> int:
    print("1..Tét: páros")
    print("2..Tét: páratlan")
    print("3..Tét: 1-18")
    print("4..Tét: 19-36")
    print("\n0..Kilépés")

    return input("\nVálasztás: ")

def osszegBekeres(maxOsszeg):
    osszeg = 0
    while osszeg <= 0 or osszeg > maxOsszeg:
        informacio(maxOsszeg)
        osszeg = int(input('Mekkora összeget tesz fel? '))
    return osszeg

def sorsolas():
    szam = random.randint(0, 36)
    print(f"A gurított szám: {szam}")
    return szam