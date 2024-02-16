class Peak:
    def __init__(self, row:str) -> None:
        splitted = row.split(';')
        self.name = splitted[0]
        self.mountain = splitted[1]
        self.height = int(splitted[2])