jegy = input("Kérem az érdemjegyet: ")

if jegy == '1':
    print("Az érdemjegy: elégtelen")
elif jegy == '2':
    print("Az érdemjegy: elégséges")
elif jegy == '3':
    print("Az érdemjegy: közepes")
elif jegy == '4':
    print("Az érdemjegy: jó")
elif jegy == '5':
    print("Az érdemjegy: jeles")
else:
    print("Ilyen osztályzat nem létezik!")