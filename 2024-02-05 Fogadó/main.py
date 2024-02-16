from functions import *

read_from_file()

print(f"2. feladat:\nFoglalások száma: {len(foglalasok)}")

print("3. feladat: ")

teach = input("Adjon meg egy nevet: ")

appointments = search_for_appointment(teach)
if appointments > 0:
    print(f"{teach} néven {appointments} időpontfoglalás van.")
else:
    print("A megadott néven nincs időpontfoglalás.")

appointment = input("Adjon meg egy érvényes időpontot (pl. 17:10): ")

search_for_teachers(appointment)

free_appointments()