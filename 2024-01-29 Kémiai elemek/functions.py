from chemistry import Chemistry

compounds: list[Chemistry] = []

def read_from_file():
    file = open("felfedezesek.csv", 'r', encoding="utf-8")
    file.readline()
    for comp in file:
        compounds.append(Chemistry(comp))
    file.close()

def BC():
    i = 0
    for comp in compounds:
        if comp.year == -1:
            i += 1
    return i

def input_():
    s = ' '
    while s == 0 or len(s) > 2 or s.lower()[0] < 'a' or s.lower()[0] > 'z' or (len(s) == 2 and s.lower()[1] < 'a') or (len(s) == 2 and s.lower()[1] > 'z'):
        s = input("5. feladat: Kérek egy vegyjelet: ")
    return s

def search(sign:str):
    for comp in compounds:
        if sign.lower() == comp.chemical_sign.lower():
            return comp
        
def longest_wait():
    max_year = 0
    for i in range(0, len(compounds)-1):
        if compounds[i].year !=-1:
            if compounds[i+1].year - compounds[i].year > max_year:
                max_year = compounds[i+1].year - compounds[i].year
    return max_year