from competitor import Competitor

competitors: list[Competitor] = []

def read_from_file():
    file = open("Selejtezo2012.txt", 'r', encoding="utf-8")
    file.readline()
    for row in file:
        competitors.append(Competitor(row))
    file.close()

def above_78m():
    i = 0
    for comp in competitors:
        if comp.throws[2] == -2:
            i += 1
    return i

def champion():
    best_throw = competitors[0]
    for c in competitors[1:]:
        if c.result() > best_throw.result():
            best_throw = c
    return best_throw

def write_to_file():
    file = open("Dontos2012.txt", 'w', encoding="utf-8")
    file.write("Helyezés;Név;Csoport;Nemzet;NemzetKód;Sorozat;Eredmény\n")
    for i in range(1, 13):
        best_throw = competitors[0]
        for c in competitors[1:]:
            if c.result() > best_throw.result():
                best_throw = c
        file.write(f'{i};{best_throw.name};{best_throw.group};{best_throw.country};{best_throw.code};{best_throw.series};{best_throw.result()}\n')
        competitors.remove(best_throw)
    file.close()