from functions import *
egyenleg = 1000
m = ''

while m != '0':
    informacio(egyenleg)
    m = menu()

    if m == '1' or '2':
        tet = osszegBekeres(egyenleg)
        match m:
            case '1':
                y = 0
            case '2':
                y = 1
        szam = sorsolas()
        if szam == 0 or szam % 2 != y:
            egyenleg -= tet
            print(f"VESZTETT, az új egyenlege: {egyenleg}$")
        else:
            egyenleg += tet
            print(f"NYERT, az új egyenleg: {egyenleg}$")
    else:
        informacio(egyenleg)
        print("Viszon látásra!")
        
    input("\nENTER")