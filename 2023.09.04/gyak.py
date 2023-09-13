import math

print("Hello World!")

# kúp felszín térfogat

r = float(input("A kúp alapjának sugara: "))

m = float(input("A kúp magassága: "))

A = r * r * math.pi + r * math.pi * math.sqrt(r * r + m * m)

V = (r * r * math.pi * m) / 3

print(f"A kúp felszíne: {A:.2f}cm2")

print(f"A kúp térfogata: {V:.2f}cm3")

