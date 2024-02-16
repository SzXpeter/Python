class Competitor:
    def __init__(self, row:str):
        data = row.strip().split(';')
        # Név;Csoport;NemzetÉsKód;D1;D2;D3
        self.name = data[0]
        self.group = data[1]
        self.country_and_code = data[2]
        self.series = f"{data[3]};{data[4]};{data[5]}"

        self.throws = []
        for i in range(3, 6):
            if data[i] == 'X':
                self.throws.append(-1)
            elif data[i] == '-':
                self.throws.append(-2)
            else:
                self.throws.append(float(data[i].replace(',', '.')))

    def result(self):
        longest_throw = self.throws[0]
        for t in self.throws[1:]:
            if t > longest_throw:
                longest_throw = t
        return longest_throw
    
    def code(self):
        return self.country_and_code[-4:-1]
    
    def country(self):
        return self.country_and_code[0:-6]
        