class Szakasz:
    def __init__(self, sor: str) -> None:
        # Sumeg, vasutallomas;Sumeg, buszpalyaudvar;1,208;16;6;n
        adatok = sor.strip().split(';')

        self.honnan = adatok[0]
        self.hova = adatok[1]
        self.tavolsag = float(adatok[2].replace(',', '.'))
        self.fel = int(adatok[3])
        self.le = int(adatok[4])
        '''
        if adatok[5] == 'i':
            self.pecsetelohely = True
        else:            
            self.pecsetelohely = False
        '''
        self.pecsetelohely = (adatok[5] == 'i')

    def HianyosNev(self) -> bool:
        if not self.pecsetelohely:
            return False
        return "pecsetelohely" not in self.hova