from os import system
from helsinki1952 import Hell

helsinki: list[Hell] = []

def main():
    system("cls")
    read()
    print(f"3. feladat: {number_of_hungarians()}")

    print("4. feladat")
    medals()

    print(f"5. feladat:\nOlimpiai pontok száma: {olimpic_point()}")

    print("6. feladat:")
    torna_vs_uszas()

    write()

    print("8. feladat:")
    most_sportpeople()


def read():
    f = open("helsinki.txt", 'r', encoding="utf-8")
    for row in f:
        helsinki.append(Hell(row))
    f.close()

def number_of_hungarians():
    i = 0
    for hel in helsinki:
        i += 1
    return i

def medals():
    first = 0
    second = 0
    third = 0
    for hel in helsinki:
        match hel.placement:
            case 1:
                first += 1
            case 2:
                second += 1
            case 3:
                third += 1
    print(f"Arany: {first}")
    print(f"Ezüst: {second}")
    print(f"Bronz: {third}")
    print(f"Összesen: {first+second+third}")

def olimpic_point():
    points = 0
    for hel in helsinki:
        match hel.placement:
            case 1:
                points += 7
            case 2:
                points += 5
            case 3:
                points += 4
            case 4:
                points += 3
            case 5:
                points += 2
            case 6:
                points += 1
    return points

def torna_vs_uszas():
    torna = 0
    uszas = 0
    for hel in helsinki:
        if hel.sport == "torna":
            torna += 1
        elif hel.sport == "uszas":
            uszas += 1

    if uszas > torna:
        print("Uszas sportágban szereztek több érmet")
    elif uszas < torna:
        print("Torna sportágban szereztek több érmet")
    else:
        print("Egyenlő volt az érmek száma")

def write():
    f = open("helsinki2.txt", 'w', encoding = "utf-8")
    h = 0
    for hel in helsinki:
        match hel.placement:
            case 1:
                h = 7
            case 2:
                h = 5
            case 3:
                h = 4
            case 4:
                h = 3
            case 5:
                h = 2
            case 6:
                h = 1
        if hel.sport == "kajakkenu":
            i = "kajak-kenu"
        else:
            i = hel.sport
        f.write(f"{hel.placement} {hel.team_size} {h} {i} {hel.category}\n")

    f.close()

def most_sportpeople():
    i = 0
    biggest = 0
    biggest_list = []
    while i < len(helsinki) - 1:
        if biggest < helsinki[i].team_size:
            biggest = helsinki[i].team_size
            biggest_list = helsinki[i]
        i += 1
    print(f"Helyezés: {biggest_list.placement}")
    print(f"Sportág: {biggest_list.sport}")
    print(f"Versenyszám: {biggest_list.category}")
    print(f"Sportolók száma: {biggest_list.team_size}")

main()