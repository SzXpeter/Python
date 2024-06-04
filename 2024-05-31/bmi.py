mass = float(input("Kérem a test tömeget (kg): "))
height = float(input("Kérem a test magasságot (m): "))
bmi = mass/(height ** 2)
print(f"A testtömeg indexed: {bmi:.2f}")

if bmi > 25:
    print("Túlsúlyos vagy.")
elif bmi < 20:
    print("Sovány vagy.")
else:
    print("Normális a testalkatod!")