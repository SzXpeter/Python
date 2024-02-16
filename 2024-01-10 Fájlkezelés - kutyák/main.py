from kutya import Kutya
import os

kutyak: list[Kutya] = []

def main():
    load_from_file()
    v = ''
    while v != '0':
        v = menu()
        match v:
            case '1':
                lista()
            case '2':
                uj()
                save_to_file()
            case '3':
                eladas()
                save_to_file()
            case '4':
                etetes()
                save_to_file()
            case '5':
                futtatas()
                save_to_file()

def menu():
    os.system('cls')
    print('1..Kutyák listája')
    print('2..Új kutya')
    print('3..Kutya eladása')
    print('4..Kutya etetése')
    print('5..Kutya futtatása')
    print('0..Kilépés')
    return input('\nVálasztás: ')

def lista():
    os.system('cls')
    for k in kutyak:
        print(f'{k.name}: {k.breed}, {k.allapot()}')

    input('\n<Enter>')

def uj():
    os.system('cls')
    name = ''
    while name == '':
        name = input('A kutya neve: ')
    
    breed = ''
    while breed == '':
        breed = input('A kutya fajtája: ')

    k = Kutya(name, breed)
    kutyak.append(k)

def eladas():
    k = keres()
    if k != None:
        kutyak.remove(k)
        print('Sikeres eladás')

    input('\n<Enter>')

def etetes():
    k = keres()
    if k != None:
        try:
            k.eszik()
            print('Nyam-nyam')
        except Exception as e:
            print(e)

    input('\n<Enter>')

def futtatas():
    k = keres()
    if k != None:
        try:
            k.mozog()
            print('Hhhhhhhh')
        except Exception as e:
            print(e)

    input('\n<Enter>')

def keres() -> Kutya:
    os.system('cls')
    name = ''
    while name == '':
        name = input('A kutya neve: ')

    i = 0
    while i < len(kutyak) and kutyak[i].name != name:
        i += 1
    
    if i < len(kutyak):
        return kutyak[i]
    
    print('Ilyen nevű kutya nincs a listában')
    return None

def load_from_file():
    f = open('kutyak.txt', 'r', encoding = 'utf-8')
    f.readline()
    for row in f:
        data = row.strip().split(';')
        kutya = Kutya(name = data[0],
                     breed = data[1],
                     health = int(data[2]))
        kutyak.append(kutya)
    f.close()

def save_to_file():
    f = open("kutyak.txt", 'w', encoding = "utf-8")
    f.write('name;breed;health\n')
    for kutya in kutyak:
        f.write("{0};{1};{2}\n".format(
            kutya.name,
            kutya.breed,
            kutya.health))
    f.close()
main()