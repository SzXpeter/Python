def tipp() -> str:
    v = ''
    while v != 'a' and v != 'b' and v != 'c':
        print("\ta: 1-es vagy 2-es")
        print("\tb: 3-es vagy 4-es")
        print("\tc: 5-es vagy 6-es")
        v = input("Választás:")
    return v

def tet(penz: int):
    t = 0
    while t <= 0 or t > penz:
        t = int(input('Mekkora összeget kockáztat? '))
    return t