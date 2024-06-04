import random
print("2.feladat: Halmaz-e")

def halmaz_e(list):
    return len(list) != len(set(list))

for i in range(8):
    list = []
    for j in range(5):
        list.append(random.randint(0, 9))
    print(f"{i+1}. {list}", end=" -> ")
    if halmaz_e(list):
        print("Halmaznak nem tekinthető!")
    else:
        print("Halmaznak tekinthető!")
