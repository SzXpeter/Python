from functions import *
from os import system

system("cls")

print("1. feladat: az 52. hét számai")
last_week = l_input()

print("2. feladat")
last_week.sort()

for l in last_week:
    print(f"\t{l}", end='')

read_from_file()
print("\n3. feladat")
gub = int(input("\tKérem a hetet: "))

print(f"4. feladat: a(z) {gub}. hét nyerőszámai:")
for num in lottery_nums[gub-1].lottery_numbers:
    print(f"\t{num}", end='')

all_numbers: list[int] = []
for i in range(1, 91):
    all_numbers.append(i)

for week in lottery_nums:
    for num in week.lottery_numbers:
        if num in all_numbers:
            all_numbers.remove(num)

print("\n5. feladat")

if len(all_numbers) == 0:
    print("Nem volt olyan szám, amit nem húztak ki.")
else:
    print("Volt(ak) olyan szám(ok), ami(ke)t nem húztak ki")