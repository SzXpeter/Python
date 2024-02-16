from peaks import *
import os

os.system("cls")
load_from_file()

print(f"3. feladat: Hegycsúcsok száma: {count()} db")

print(f"4. feladat: Hegycsúcsok átlagos magassága: {average_height()} m")

peak = highest_mountain()
print(f"5. feladat: a legmagasabb hegycsúcs adatai:")
print(f"\tNév: {peak.name}")
print(f"\tHegység: {peak.mountain}")
print(f"\tMagasság: {peak.height} m")

print("6. feladat: ", end='')
inp = int(input("Kérek egy magasságot: "))
peak = higher_than(inp)
if peak == None:
    print(f"\tNincs {inp} m-nél magasabb hegycsúcs")
else:
    print(f"\tVan {inp} m-nél magasabb hegycsúcs a {peak.name}")

print(f"7. feladat: 3000 lábnál magasabb hegcsúcsok száma {higher_then_3000f()}")



write_to_file()