
x = int(input("Írja be az oldalak számát: "))
K = 0

if x <= 2:
    print("Nincs ilyen sokszög!")
else:
    for i in range(x):
        oldal_hossz = float(input(f"Adja meg a(z) {i + 1}. oldal hosszát: "))
        K += oldal_hossz

print(f"A sokszög kerülete: {K}")