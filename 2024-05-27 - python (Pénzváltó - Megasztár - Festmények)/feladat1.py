penznem = input("Eurót (EUR) vagy forintot (HUF) akarsz váltani? ")

if penznem == "EUR":
    penz = int(input("Hány eurót akarsz bevéltani? "))
    print(f"{penz} euróért {penz * 365} forintot kapsz.")
else:
    penz = int(input("Hány forintot akarsz bevéltani? "))
    print(f"{penz} forintért {penz / 365:.2f} eurót kapsz.")