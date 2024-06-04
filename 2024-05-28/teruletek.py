import math

def number_input(szoveg):
    szam = 0
    while True:
        try:
            szam = float(input(szoveg))
            if szam <= 0:
                raise Exception
        except:
            pass
        else:
            return szam
        
def teglalap_terulet():
    a = number_input("Kérem az első oldalt: ")
    b = number_input("Kérem a második oldalt: ")
    return a * b

def haromszog_terulete():
    a = number_input("Kérem az első oldalt: ")
    b = number_input("Kérem a második oldalt: ")
    c = number_input("Kérem a harmadik oldalt: ")
    s = (a + b + c) / 2
    T = 0
    try:
        T = math.sqrt(s*(s-a)*s*(s-b)*s*(s-c))
        if T == 0:
            raise Exception
    except:
        return "Nem lehet megszerkeszteni"
    else:
        return T


print(teglalap_terulet())
print(haromszog_terulete())