class Chemistry:
    def __init__(self, row: str):
        data = row.strip().split(';')
        # Év;Név;Vegyjel;Rendszám;Felfedező
        if data[0] == "Ókor":
            self.year = -1
        else:
            self.year = int(data[0]) 
        self.name = data[1]
        self.chemical_sign = data[2]
        self.number = int(data[3])
        self.discoverer = data[4]