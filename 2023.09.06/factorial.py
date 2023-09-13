"""
import math

x = int(input("Kérem a számot: "))

print(math.factorial(x))
"""

x = int(input("Kérem a számot: "))

fakt = 1

for i in range(x):
    fakt *= i + 1

print(f"A szám faktoriálisa: {fakt}")