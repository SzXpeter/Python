import random

pontok = []
for i in range(5):
    pontok.append(random.randint(1, 10))

def osszpont(PontokParam: list[int]):
    PontokParam.remove(max(PontokParam))
    return sum(PontokParam)

print(f"{pontok} -> összpontszám: {osszpont(pontok)} pont")