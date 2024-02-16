from functions import *
from os import system

read_from_file()
system("cls")

print(f"5. feladat: Versenyzők száma a selejtezőben: {len(competitors)} fő")

print(f"6. feladat: 78,00 méter feletti eredménnyel továbbjutott: {above_78m()} fő")

champ = champion()
print("9. feladat: A selejtező nyertese:")
print(f"\tNév: {champ.name}")
print(f"\tCsoport: {champ.group}")
print(f"\tNemzet: {champ.country()}")
print(f"\tNemzet kód: {champ.code()}")
print(f"\tSorozat: {champ.series[0]};{champ.series[1]};{champ.series[2]}")
print(f"\tEredmény: {str(champ.result()).replace('.', ',')}")

write_to_file()