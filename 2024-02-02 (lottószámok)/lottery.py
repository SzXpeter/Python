class Lottery:
    def __init__(self, row:str):
        data = row.strip().split(' ')
        self.lottery_numbers = []
        for d in data:
            self.lottery_numbers.append(int(d))
