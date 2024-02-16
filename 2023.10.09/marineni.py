from random import randint

mai_napi_eper = 0
minimum = 10
min_napok = ''
ossz = 0
mari_neni_haszon = 0
pista_bacsi_haszon = 0

for i in range(1, 31):
    mai_napi_eper = randint(0, 10)
    print(f"{i}. {mai_napi_eper}kg")
    if mai_napi_eper < minimum:
        minimum = mai_napi_eper
        min_napok = ''
    
    if mai_napi_eper == minimum:
        min_napok += f"{i}. "

    ossz += mai_napi_eper

print(f"Összes eper: {ossz}kg.")

if minimum == 0:
    print(f"{min_napok} napo(ko)n nem szedett.")
else:
    print(f"{min_napok} napo(ko)n szedett a legkevesebbet.")

mari_neni_haszon = (ossz * 1200) - (ossz * 450)
print(f"Mari néni {mari_neni_haszon:,}Ft haszont szerezne.".replace(',', ' '))

pista_bacsi_haszon = (ossz * 500) - (ossz * 450)
print(f"Mari néni {pista_bacsi_haszon:,}Ft haszont szerezne.".replace(',', ' '))