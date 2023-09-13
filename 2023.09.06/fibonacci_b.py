#kérjen be egy egész számot a felhasználótól és írja ki a fibonacci sorozat adott elemét


f_sorozat_sorszam = int(input("Adja meg egy fibonacci sorozat elemének a sorszámát: "))

if f_sorozat_sorszam < 0:
    print("Ilyen fibonacci szám nincs")

elif f_sorozat_sorszam == 0:
    print(f"A fibonacci sorozat 0. eleme 0 értékű.")

elif f_sorozat_sorszam <= 2:
    print(f"A fibonacci sorozat {f_sorozat_sorszam}. eleme 1 értékű.")

else:
    a = 1
    b = 1

    for i in range(f_sorozat_sorszam - 2):
        c = a + b
        a = b
        b = c

    print(f"A fibonacci sorozat {f_sorozat_sorszam}. eleme {c} értékű.")