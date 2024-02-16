import os
from nobel import Nobel

nobels: list[Nobel] = []

def main():
    read()
    os.system("CLS")
    print(f"3. feladat: {Arthur()}")

    print(f"4. feladat: {Irodalmi()}")

    n = peace()
    print("5. feladat:")
    for p in n:
        print(f"\t{p}")

    n = Curie()
    print("6. feladat")
    for p in n:
        print(f"\t{p}")

    n = type_count()
    print("6. feladat")
    print(f"\tfizikai\t\t\t{n[0]} db")
    print(f"\tkémiai\t\t\t{n[1]} db")
    print(f"\torvosi\t\t\t{n[2]} db")
    print(f"\tirodalmi\t\t{n[3]} db")
    print(f"\tbéke\t\t\t{n[4]} db")
    print(f"\tközigazgatási\t\t{n[5]} db")

    write()

def read():
    f = open("nobel.csv", 'r', encoding="utf-8")
    f.readline()
    for row in f:
        nobels.append(Nobel(row))
    f.close()

def Arthur():
    for n in nobels:
        if n.first_name == "Arthur B." and n.last_name == "McDonald":
            return n.type

def Irodalmi():
    for n in nobels:
        if n.year == 2017 and n.type == "irodalmi":
            return f"{n.first_name} {n.last_name}"

def peace():
    peace_nobel = []
    for n in nobels:
        if n.year < 1990:
            return peace_nobel
        elif n.type == "béke":
            peace_nobel.append(f"{n.year}: {n.first_name}")

def Curie():
    curie_family = []
    for n in nobels:
        if "Curie" in n.last_name:
            curie_family.append(f"{n.year}: {n.first_name} {n.last_name}({n.type})")
    return curie_family

def type_count():
    types = [0, 0, 0, 0, 0, 0]
    for n in nobels:
        if n.type == "fizikai":
            types[0] += 1
        elif n.type == "kémiai":
            types[1] += 1
        elif n.type == "orvosi":
            types[2] += 1
        elif n.type == "irodalmi":
            types[3] += 1
        elif n.type == "béke":
            types[4] += 1
        else:
            types[5] += 1
    return types

def write():
    nobels.reverse()
    f = open("orvosi.txt", 'w', encoding="utf-8")

    for n in nobels:
        if n.type == "orvosi":
            f.write("{0}:{1} {2}\n".format(
                n.year,
                n.first_name,
                n.last_name))

    f.close()
    nobels.reverse()

main()