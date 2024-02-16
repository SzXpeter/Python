class Auto:
    '''rendszam: str
    tipus: str
    kmOraAllas: int
    fogyasztas: float
    uzemanyagMennyiseg: float
    uzemanyagTartalyMeret: int'''

    # constructor
    def __init__(self, rendszam: str, tipus: str, kmOraAllas: int, fogyasztas: float, uzemanyagMennyiseg: float, uzemanyagTartalyMeret: int):
        self.rendszam = rendszam
        self.tipus = tipus
        self.kmOraAllas = kmOraAllas
        self.fogyasztas = fogyasztas
        self.uzemanyagMennyiseg = uzemanyagMennyiseg
        self.uzemanyagTartalyMeret = uzemanyagTartalyMeret

    def utazas(self, ujKmOraAllas: int):   # metódus
        if ujKmOraAllas <= self.kmOraAllas:
           raise Exception("Hibás adat: az új km óra állás nem lehet kisebb, se egyenlő , az induló értékkel.")
        else:
            km = ujKmOraAllas - self.kmOraAllas
            uzemanyagLiter = (km / 100) * self.fogyasztas
            if uzemanyagLiter > self.uzemanyagMennyiseg:
                raise Exception("Hibás adat: a szükséges üzemanyag nem volt az autóban.")
            else:
                self.kmOraAllas = ujKmOraAllas
                self.uzemanyagMennyiseg -= uzemanyagLiter
                print("Az út rögzítve lett.")