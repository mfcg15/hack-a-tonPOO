from classes.jugador import Jugador

class Ninja(Jugador):

    def __init__(self, name):
        super().__init__(name)
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def attack_kunai(self,attack):
        print(f"{self.name} a utilizado {attack}")