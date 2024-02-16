class Hell:
    def __init__(self, row: str):
        data = row.strip().split(' ')
        self.placement = int(data[0])
        self.team_size = int(data[1])
        self.sport = data[2]
        self.category = data[3]