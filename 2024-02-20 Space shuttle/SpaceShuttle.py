from kuldetes import Kuldetes

kuldetesek: list[Kuldetes] = []

file = open('kuldetesek.csv', 'r', encoding="utf-8")
for row in file:
    kuldetesek.append(Kuldetes(row))
file.close()

print("3. feladat:")
print(f"\tÖsszesen {len(kuldetesek)} alkalommal indítottak űrhajót.")

print("4. feladat: ")
ossz = 0
for k in kuldetesek:
    ossz += k.legenyseg
print(f"\t{ossz} utas indult az űrbe összesen.")

print("5. feladat")
db = 0
for k in kuldetesek:
    if k.legenyseg < 5:
        db += 1
print(f"\tÖsszesen {db} alkalommal küldtek kevesebb, mint 5 embert az űrbe.")

print("6. feladat:")
i = 0
while i < len(kuldetesek) and (kuldetesek[i].ursiklo != "Columbia" or kuldetesek[i].landolas != "nem landolt"):
    i += 1

if i < len(kuldetesek):
    print(f"\t{kuldetesek[i].legenyseg} aztronauta volt a Columbia fedélzetén annak utolsó útján.")
else:
    print("Az állományban nem szerepel a Columbia utolsó útja.")

print("7. feladat:")
leghosszabb: Kuldetes = kuldetesek[0]
for k in kuldetesek[1:]:
    if k.osszes_ora > leghosszabb.osszes_ora:
        leghosszabb = k
print(f"\tA legosszabb ideig {leghosszabb.ursiklo} volt az űrben a {leghosszabb.kod} küldetes során.\nÖsszesen {leghosszabb.osszes_ora} órát volt távol a Földől")

print("8. feladat")
i = 0
ev = input("\tÉvszám: ")
for k in kuldetesek:
    if k.datum.startswith(ev):
        i += 1
if i != 0:
    print(f"\tEbben az évben {i} küldetés volt")
else:
    print("\tEbben az évben nem indult küldetés")

print("9. feladat")
i = 0
for k in kuldetesek:
    if k.landolas == "Kennedy":
        i += 1
print(f"\tA küldetése {i / len(kuldetesek) * 100:.2f}%-a fejeződött be a Kennedy űrközpontban")

urhajok = dict()
for k in kuldetesek:
    if k.ursiklo in urhajok.keys():
        urhajok[k.ursiklo] += k.osszes_ora / 24
    else:
        urhajok[k.ursiklo] = k.osszes_ora / 24

file = open("ursiklok.txt", 'w', encoding="utf-8")
for key, value in urhajok.items():
    file.write(f"{key}\t{value:.2f}\n")