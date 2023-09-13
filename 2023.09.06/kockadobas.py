import random

dobas_ossz = 0
dobas = 0

for i in range(1, 7):
    dobas = random.randint(1, 6)
    print(f"dobás... {dobas}")
    dobas_ossz += dobas

print(f"A dobások összege: {dobas_ossz}")