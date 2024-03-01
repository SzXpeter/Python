from allat import Allatfaj

allatok: list[Allatfaj] = []

for i in range(3):
    nev = input("Add meg egy állatfaj nevét! ")
    tomeg = input("Hány kilogramm a tömege a példánynak? ")
    allatok.append(Allatfaj(nev, tomeg))

legnehezebb: Allatfaj = allatok[0]
for a in allatok:
    print(f"A(z) {a.fajnev} tömege {a.tomeg} kg.")
    if a.tomeg > legnehezebb.tomeg:
        legnehezebb = a

file = open("legnehezebb.txt", 'w', encoding="utf-8")
file.write(legnehezebb.fajnev)
file.close()