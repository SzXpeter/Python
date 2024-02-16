import os
def foMenu():
    v = ''
    while v != '0' and v != '1' and v != '2' and v != '3':
        os.system("cls")
        print("1...Első menüpont")
        print("2...Második menüpont")
        print("3...Harmadik menüpont")
        print("0...Kilépés")
        v = input("\nVálasztás..")
    return v
