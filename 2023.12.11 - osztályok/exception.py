def szam_bekeres() -> int:
    x = None
    while x == None:
        try:
            x = int(input("a = "))
        except:
            x = None
    return x

print(f"A bekért szám: {szam_bekeres()}")