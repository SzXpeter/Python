import random
lista = []
n = 20
for i in range(n):
    lista.append(random.randint(100,1000))
print(lista)

s = 0
for elem in lista:
    s = s + elem

print(f"Az étlag: {s}")