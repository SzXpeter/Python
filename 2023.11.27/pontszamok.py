from os import system
from sys import exit
pontszamok = [54,74,16,52,24,81,88,25,5,18,37,6,0,19,13,95,14,99,66,58,83,19,70,89,59,93,59,41,27,57,4,77,8]

'''
Feladatok
    Menü:
        -pontszamok átlaga
        -kérdezzünk a felhasználótól egy osztályzatot -> írjuk ki hány annak megfelelő doga lett
            20pontonként megy föl a jegy
        -Legjobb dolgozat: pontsazám és sorszám
        -kérdezzünk a felhasználótól egy pontszámot -> van-e ilyen pontszámú
        -keressük meg az első 0 pontos dolgozat sorszámát
            -ha nincs akkor írjuk ki hogy nincs
'''

def main():
    while True:
        match menu():
            case '0':
                exit()
            case '1':
                atlag()
            case '2':
                osztalyzat_darab()
            case '3':
                legjobb_dolgozat()
            case '4':
                eldontes()
            case '5':
                van_e_nulla()

def menu(): 
    v = ''
    while v not in ['0', '1', '2', '3', '4', '5']:
        system("cls")
        print("1...pontszamok átlaga")
        print("2...Adott osztályzatok száma")
        print("3...Legjobb dolgozat")
        print("4...Van-e 'n' pontsazámú dolgozat")
        print("5...Van-e benne nulla")
        print("0...exit")
        v = input("\nVálasztás: ")
    return v

def atlag():
    ossz = 0
    for pont in pontszamok:
        ossz += pont
    print(f"A pontszámok átlaga: {(ossz / len(pontszamok)):.2f}")
    input("\n<ENTER>")

def osztalyzat_darab():
    system("cls")
    osztalyzat = int(input("Hányas dolgozatok számára kíváncsi? "))
    db = 0

    max = osztalyzat * 20
    if osztalyzat == 1:
        min = 0
    else:
        min = max - 19

    if osztalyzat in [1, 2, 3, 4, 5]:
        for i in pontszamok:
            if min <= i <= max:
                db += 1
        print(f"{osztalyzat}-s dolgozatból {db} db született.")
    else:
        print("Nincs ilyen osztályzat")
    input("<ENTER>")

def legjobb_dolgozat():
    system("cls")
    maxErtek = pontszamok[0]
    maxIndex = 0
    for i in range(len(pontszamok)):
        if pontszamok[i] > maxErtek:
            maxErtek = pontszamok[i]
            maxIndex = i
    print(f"A legjobb dolgozat sorszáma: {maxIndex + 1}, elért pontok száma: {maxErtek}")
    input("<ENTER>")

def eldontes():
    system("cls")
    pontszam = int(input("Kérem a pontszámot: "))
    i = 0
    while i < len(pontszamok) and pontszamok[i] != pontszam:
        i += 1
    if i < len(pontszamok):
        print("Van ilyen dolgozat!")
    else:
        print("Nincs ilyen dolgozat!")

    input("<ENTER>")

def van_e_nulla():
    system("cls")
    i = 0
    while i < len(pontszamok) and pontszamok[i] != 0:
        i += 1
    if i < len(pontszamok):
        print(f"Az első 0 pontos doga a(z) {i + 1}. doga volt.")
    else:
        print("Nincs 0 pontos dolgozat!")

    input("<ENTER>")

main()