class Foglalas:
    def __init__(self, row:str):
        # Csorba Ede 16:30 2017.10.28-18:48
        data = row.strip().split(' ')
        self.name = data[0] + ' ' + data[1]
        self.appointment = data[2]
        self.date = data[3]

        oopp = self.appointment.split(':') 
        self.percek = int(oopp[0]) * 60 + int(oopp[1])