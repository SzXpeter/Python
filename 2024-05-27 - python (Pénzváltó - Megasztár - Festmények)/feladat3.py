class Festmeny:
    def __init__(self, row):
        data = row.strip().split(";")
        self.cim = data[0]
        self.festo_neve = data[1]
        self.keszites_eve = int(data[2])
        self.becsult_ertek = int(data[3])
        self.eredeti_ar = int(data[4])
        self.eladas_eve = data[5]

festmenyek: list[Festmeny] = []

file = open("paintings.txt", 'r', encoding="utf-8")
file.readline()
for row in file:
    festmenyek.append(Festmeny(row))
file.close()

print(f"3.3 feladat: A fájlban tárolt festmények száma: {len(festmenyek)}")

i = 0
for festmeny in festmenyek:
    if festmeny.festo_neve == "Pablo Picasso":
        i += 1

print(f"3.4 feladat: A Pablo Picasso képek száma: {i} darab.")

legdragabb_festmeny = festmenyek[0]
for festmeny in festmenyek:
    if festmeny.becsult_ertek > legdragabb_festmeny.becsult_ertek:
        legdragabb_festmeny = festmeny

print(f"A legdrágább kép festője: {legdragabb_festmeny.festo_neve}, a kép címe: {legdragabb_festmeny.cim}, becsült értéke: {legdragabb_festmeny.becsult_ertek}")

i = 0
while i < len(festmenyek):
    if festmenyek[i].becsult_ertek <= festmenyek[i].eredeti_ar:
        break
    i += 1

if i < len(festmenyek):
    print(f"3.6 feladat: Van olyan festmény, amelynek a becsült értéke nem haladja meg az eredeti árát.")
else:
    print(f"3.6 feladat: Nincs olyan festmény, amelynek a becsült értéke nem haladja meg az eredeti árát.")