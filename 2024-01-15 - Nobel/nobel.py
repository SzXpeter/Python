class Nobel:
    def __init__(self, row: str):
        data = row.strip().split(';')
        self.year = int(data[0])
        self.type = data[1]
        self.first_name = data[2]
        self.last_name = data[3]