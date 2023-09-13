maxpont = float(input("Kérem a maximum pontszámot: "))
elertpont = float(input("Kérem az elért pontszámot: "))

szazalek = elertpont / maxpont

if szazalek >= .85:
    print("Az érdemjegy: jeles")
elif szazalek >= .7:
    print("Az érdemjegy: jó")
elif szazalek >= .55:
    print("Az érdemjegy: közepes")
elif szazalek >= .4:
    print("Az érdemjegy: elégséges")
else:
    print("Az érdemjegy: elégtelen")