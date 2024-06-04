import random

osveny = []

for i in range(25):
    osveny.append(random.randint(0, 1))

def attud_e_kelni(osveny):
    i = 0
    pocsolya_egyhuzamban = 0
    while i < len(osveny):
        if osveny[i] == 1:
            pocsolya_egyhuzamban += 1
        else:
            pocsolya_egyhuzamban = 0
        if pocsolya_egyhuzamban == 4:
            break
        i += 1
    return i < len(osveny)

print(osveny)
if attud_e_kelni(osveny):
    print("Piroska nem tud átkelni száraz lábbal az ösvényen.")
else:
    print("Piroska át tud kelni száraz lábbal az ösvényen.")