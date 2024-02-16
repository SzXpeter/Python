import os
from auto import Auto

autok: list[Auto] = [
        Auto("ABC-123", "Audi RS6", 23245, 14.5, 23.5, 73),
        Auto(rendszam = 'DEF-456', tipus = 'Vw Passat 1.9TDI', fogyasztas = 7.5, kmOraAllas = 122542, uzemanyagMennyiseg = 3.4, uzemanyagTartalyMeret = 68)
    ]

def main():
    v = ''
    while v != '0':
        v = menu()
        match v:
            case '1':
                autoLista()
            case '2':
                ujAuto()
            case '3':
                autoTorles()
            case '4':
                ujUt()
            case '5':
                pass

def menu() -> str:
    os.system('cls')
    print('1..Autók listája')
    print('2..Új autó rögzítése / beszerzése')
    print('3..Autó törlése / eladása')
    print('4..Megtett út rögzítése')
    print('5..Tankolás rögzítése')
    print('0..Kilépés')

    return input('\nVálasztás: ')

def autoLista():
    os.system('cls')
    for a in autok:
        print(a.rendszam)
        print(f'\t{a.tipus}, {a.kmOraAllas} km, {a.fogyasztas} l/100km, {a.uzemanyagMennyiseg}/{a.uzemanyagTartalyMeret} l')

    input('<ENTER>')

def ujAuto():
    os.system('cls')
    rendszam = input('Az új autó rendszáma: ')
    tipus = input('Típusa: ')
    kmOraAllas = int(input('Km óra állása: '))
    fogyasztas = float(input('Fogyasztása (liter / 100km): '))
    uzemanyagMennyiseg = float(input('Jelenlegi üzemanyag szint/mennyiség (l): '))
    uzemanyagTartalyMeret = int(input('Üzemanyag tartály mérete (l): '))

    autok.append(Auto(rendszam, tipus, kmOraAllas, fogyasztas, uzemanyagMennyiseg, uzemanyagTartalyMeret))
    print('\nSikeres rögzítés')
    input('<ENTER>')

def autoKereses(szoveg: str) -> Auto:
    rendszam = input(szoveg)
    i = 0
    while i < len(autok) and autok[i].rendszam != rendszam:
        i += 1
    if i < len(autok):
        return autok[i]
    return None

def autoTorles():
    os.system('cls')
    a = autoKereses("Kérem a törlendő autó rendszámát: ")
    if a == None:
        print('Az autó nem található')
    else:
       autok.remove(a) 
       print('Sikeres törlés')
    input('<ENTER>')

def ujUt():
    os.system('cls')
    a = autoKereses("Kérem az autó rendszámát: ")
    if a == None:
        print('Az autó nem található')
    else:
        ujKmOraAllas = int(input("Az autó km óra állása az út után: "))
        try:
            a.utazas(ujKmOraAllas)
            print("Sikeres rögzítés!")
        except Exception as e:
            print(e)

    input('<ENTER>')

main()