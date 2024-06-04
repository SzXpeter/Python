class Fogadasi_fordulo:
    def __init__(self, row):
        data = row.strip().split(';')
        self.ev = data[0]
        self.het = data[1]
        self.fordulo = data[2]
        self.t13p1 = int(data[3])
        self.ny13p1 = int(data[4])
        self.eredmenyek = data[5]

toto_list: list[Fogadasi_fordulo] = []

file = open("toto.txt", 'r', encoding="UTF-8")
file.readline()
for row in file:
    toto_list.append(Fogadasi_fordulo(row))

print("3. feladat: Toto")
print("3.1 feladat: Adatok beolvasása és tárolása")
print(f"3.2 feladat: Fogadási fordulók száma: {len(toto_list)}")

teli_talalat = 0
for toto in toto_list:
    teli_talalat += toto.t13p1

print(f"3.3 feladat: Teli találatos szelvények száma: {teli_talalat} darab")

i = 0
while i < len(toto_list):
    if not "X" in toto_list[i].eredmenyek:
        break
    i += 1

if i < len(toto_list):
    print("3.4 feladat: Volt döntetlen mentes forduló")
else:
    print("3.4 feladat: Nem volt döntetlen mentes forduló")