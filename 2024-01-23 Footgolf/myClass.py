class Footgolf:
    def __init__(self, row: str):
        data = row.strip().split(';')
        self.name = data[0]
        self.category = data[1]
        self.association = data[2]
        self.points: list[int] = []

        for p in data[3:]:
            self.points.append(int(p))

    def total_score(self):
        total_score = 0

        temp = []
        for p in self.points:
            temp.append(p)
        
        for i in range(2):
            min = temp [0]
            for p in temp:
                if p < min:
                    min = p

            if min > 0:
                total_score += 10
            temp.remove(min)

        for t in temp:
            total_score += p
        
        return total_score
            