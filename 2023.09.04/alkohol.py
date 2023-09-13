ma_ev = 2023
ma_ho = 9
ma_nap = 4

szul_ev = int(input("Születési év: "))

if ma_ev - 18 > szul_ev:
    print("Vehet piát!")
elif ma_ev - 18 < szul_ev:
    print("Nem vehet piát!")
else:
    szul_ho = int(input("Születési hónap: "))
    if ma_ho < szul_ho:
        print("Vehet piát!")
    elif ma_ho < szul_ho:
        print("Nem vehet piát!")
    else:
        szul_nap = int(input("Születési nap: "))
        if ma_nap > szul_nap:
            print("Vehet piát!")
        elif ma_nap < szul_nap:
            print(f"Gyere vissza {szul_nap - ma_nap} nap múlva")
        else:
            print("Boldog születésnapot!")
