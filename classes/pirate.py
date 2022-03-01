from classes.jugador import Jugador

class Pirate (Jugador):

    def __init__(self, name):
        super().__init__(name)
        self.strength = 5
        self.speed = 3
        self.health = 100

    def attack_sword(self,attack):
        print(f"{self.name} a utilizado {attack}")
