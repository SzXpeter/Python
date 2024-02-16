class Kutya:

    def __init__(self, name, breed, health = 50):
        self.name = name
        self.breed = breed
        if health > 100 or health <= 0:
            raise Exception("Hibás életerő érték")
        self.health = health    # max 100

    def allapot(self) -> str:
        if self.health < 20:
            return 'éhes'
        if self.health < 40:
            return 'fáradt'        
        if self.health < 80:
            return 'normál'                
        return 'életvidám'
    
    def eszik(self):
        if self.health > 80:
            raise Exception('Az eb nem elég éhes')
        else:
            self.health += 20

    def mozog(self):
        if self.health < 20:
            raise Exception('Az eb inkább enne')
        else:
            self.health -= 10
            