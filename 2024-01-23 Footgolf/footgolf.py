from functions import *
from os import system

system('cls')
read_from_file()

print(f"3. feladat: Versenyzők száma: {len(footgolfers)}")

print(f"4. feladat: A női versenyzők aránya: {(woman_percent() * 100):.2f} %")

foot = woman_champion()
print("6.feladat: A bajnok női versenyző ")
print(f"\tNév: {foot.name}")
print(f"\tNév: {foot.association}")
print(f"\tNév: {foot.total_score()}")

write_to_file()