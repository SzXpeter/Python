class Kutya:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.HP = 50 # max 50

    def allapot(self) -> str:
        if self.HP < 20:
            return "éhes"
        if self.HP < 40:
            return "fáradt"
        if self.HP < 80:
            return "normál"
        return "életvidám"
    
    def eszik(self):
        if self.HP > 80:
            raise Exception("Az eb nem elég éhes")
        else:
            self.HP += 20

    def mozog(self):
        if self.HP < 20:
            raise Exception("Az eb nem akar sétálni")
        else:
            self.HP -= 10