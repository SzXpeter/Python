#kérjen be egy egész számot a felhasználótól és írja ki a fibonacci sorozat adott elemét

f_sorozat_sorszam = int(input("Adja meg egy fibonacci sorozat elemének a sorszámát: "))

if f_sorozat_sorszam < 0:
    print("Ilyen fibonacci szám nincs")

elif f_sorozat_sorszam == 0:
    print(f"A fibonacci sorozat 0. eleme 0 értékű.")

elif f_sorozat_sorszam <= 2:
    print(f"A fibonacci sorozat {f_sorozat_sorszam}. eleme 1 értékű.")
    
else:
    x = 1
    y = 1

    for i in range(f_sorozat_sorszam - 3):
        if (i + 1) % 2 == 0:
            x += y
        else:
            y +=x

    ertek = x + y
    print(f"A fibonacci sorozat {f_sorozat_sorszam}. eleme {ertek} értékű.")