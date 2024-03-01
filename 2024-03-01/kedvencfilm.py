from filmalap import oraperc

for i in range(3):
    film = input("Adja meg egy film címét! ")
    film_perc = input("Hány perces film? ")
    print(f"A(z) {film} című film {oraperc(film_perc)} hosszú")