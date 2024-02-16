from functions import *

read_from_file()

print(f"3. feladat: Elemek száma: {len(compounds)}")

print(f"4. feladat: Felfedezések száma az ókorban: {BC()}")

compound = input_()

comp = search(compound)

print("6. feladat: Keresés")
if comp == None:
    print("\tNincs ilyen elem az adatforrásban!")
else:
    print(f"\tAz elem vegyjele: {comp.chemical_sign}")
    print(f"\tAz elem neve: {comp.name}")
    print(f"\tRendszáma: {comp.number}")
    print(f"\tFelfedezés éve: {comp.year}")
    print(f"\tFelfedező: {comp.discoverer}")

print(f"7. feladat: {longest_wait()} év volt a leghosszabb időszak két elem felfeezése között.")