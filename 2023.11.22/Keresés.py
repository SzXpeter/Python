import random

T = []
for i in range(20):
    T.append(random.randint(-2, 100))

ertek = int(input("Keresett érték: "))

i = 0
while i < len(T) and T[i] != ertek:
    i = i + 1
if i < len(T):
    print(f"A listában a {i + 1}. elem a keresett érték.")
else:
        print("A listában nem szerepel a keeesett érték")