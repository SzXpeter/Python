import random

T = []
for i in range(20):
    T.append(random.randint(-2, 100))

i = 0
while i < 20 and T[i] >= 0:
    i = i + 1

print(T)
if i < 20:
    print("A listában van negatív szám.")
else:
    print("A listában nincs negatív szám.")