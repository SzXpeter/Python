import random, os

os.system("cls")

pin = random.randint(1000, 9999)
pinInput = 0
attempts = 3

while pin != pinInput and attempts != 0:
    pinInput = int(input("Adja meg a PIN kódot: "))

    if pinInput == 123456:
        choose = input("1.. Reveal PIN\n2.. Change PIN\n...")
        if choose == '1':
            print(pin)
        elif choose == '2':
            firstChangePin = int(input("Change PIN: "))
            secondChangePin = int(input("Confirm PIN: "))
            if firstChangePin == secondChangePin:
                print("PIN-code has been changed!")
                pin = firstChangePin
            else:
                print("Incorrect!")
                attempts -= 1
    elif pinInput == pin:
        print("Sikeres azonosítás!")
    else:
        print("Incorrect!")
        attempts -= 1

if attempts == 0:
    print("Locked!")