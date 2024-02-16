# Dictionary
szotar = dict()

# elem(ek) hozzáadása
szotar["alma"] = "apple"
szotar["barack"] = "appricot"

# elemek kiírása
print(szotar) # {'alma': 'apple', 'barack': 'peach'}

for key, value in szotar.items():
    print(f"{key} = {value}")

# elem értékének módosítása -> egy adott kulcshoz tartozó érték módosítása
# (kulcs nem módosítható)
szotar["barack"] = "peach"
print(szotar)

# elem törlése -> egy adott kulcs törlése
del szotar["barack"]
print(szotar)

# Ellenőrzés: létezik-e a kulcs a szótárban
if "alma" in szotar.keys():
    print("Az alma már benne van a szotárban")
else:
    print("Az alma már benne van a szótárban")

if "barack" in szotar.keys():
    print("A barack már benne van a szotárban")
else:
    print("A barack már benne van a szótárban")