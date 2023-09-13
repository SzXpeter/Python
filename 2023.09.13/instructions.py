import random
import math

def szamHuzas1_90() -> int:
    return random.randint(1,90)

#univerzális számhúzás
def szamHuzas(maxertek):
    return random.randint(1, maxertek)

def osszeadas(x, y):
    return x + y

def kerekites(x: float):
    return int(x + 0.5)

def alapMuvelet(a, muvelet, b):
    match muvelet:

        case '+':
            return a + b
        
        case '-':
            return a - b
        
        case '*':
            return a * b
        
        case '/':
            return a / b
        
        case _:
            return None
        
def egseszSzamBekeres(szoveg: str) -> int:
    s = ''
    while not s.isdecimal():
        s = input(szoveg)
    return int(s)

def egseszSzamBekeres2(min, max, szoveg: str) -> int:
    s = ''
    while not s.isdecimal() or min > int(s) or int(s) > max:
        s = input(szoveg)
    return int(s)
    

    """
    szam = min - 1
    while not min <= szam <= max:
        szam = egseszSzamBekeres(szoveg)
    return szam
    """