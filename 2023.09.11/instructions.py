import random
import math

def instruction_1():
    for i in range(5):
        print(random.randint(1, 90), end = "\t")
    print()


def instruction_2():
    r = float(input("Adja meg a gömb sugarát: "))
    if r <= 0:   
        print("Ilyen gömb nincs!")
    else:
        V = (4 * r * r * r * math.pi) / 3
        A = 4 * r * r * math.pi
        print(f"A gömb térfogata: {format(V, '.2f')}")
        print(f"A gömb felszíne: {format(A, '.2f')}")


def instruction_3():
    n = int(input("Adja meg az összes tanuló számát: "))
    x = int(input("Adja meg a választott tanulók számát: "))
    div = x / n * 100
    print(f"{format(div, '.2f')}% esélye van, hogy kihúzzák.")


def instructions_4():
    C = 0
    for i in range(10):
        C += float(input(f"Adja meg a(z) {i + 1}. nap reggeli hőmérsékletét: "))
    C = C / 10
    print(f"A hőmérsékletek átlaga: {C}°C")