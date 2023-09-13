"""
feladat:
    készítsen menüt, amiben van 3 meüpont + a kilépés
        -lottószámok hűzás(5/90)
        -gömb felszín, térfogat
        -valószínűség számítás:
            n tanuló  jár az osztályba, x tanuló felel. Mi az esély, h megússza?
        -HF: + menüpont 10 nap reggeli hőmérsékletét --> átlag
"""
import os
from instructions import *

instr = ''
while instr != '0':
    os.system("cls")
    print("1, Lottószámok kihúzása", "\n2, Gömb felszín, térfogat kiszámítása", "\n3, Valószínűség számítás", "\n4, Reggeli hőmérséklet átlag számítás", "\n0, Kilépés")
    instr = input("\n...")
    os.system("cls")

    if instr == '1':
        print("A jövő heti lottószámok (Ha ezeket húzzák ki).")
        instruction_1()

    elif instr == '2':
        print("Gömb térfogat és felszín számolás.")
        instruction_2()

    elif instr == '3':
        print("Valószínűség számítás.")        
        instruction_3()

    elif instr == '4':
        print("A napi hőmérsékletek átlaga.")
        instructions_4()

    elif instr == '0':
        print("Viszont gépelésre!")

    else:
        print("Érvénytelen választás!")

    input("\n\nFolytatáshoz nyomjon entert")