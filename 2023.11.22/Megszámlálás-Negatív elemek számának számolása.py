import random

T = []
for i in range(100):
    T.append(random.randint(-100, 100))
print(T)

db = 0
for i in T:
    if i < 0:
        db = db + 1

print(f"A listában {db}db negatív szám van")