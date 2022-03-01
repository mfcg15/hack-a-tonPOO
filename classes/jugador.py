class Jugador :

    def __init__( self , name ):
        self.name = name
    
    def show_stats( self ):
        print(f"Name: {self.name}, Strength: {self.strength}, Speed: {self.speed}, Health: {self.health}\n")

    def attack ( self , player ):
        player.health -= self.strength
        return self

    def show_health(self):
         print(f"{self.name} tiene ahora {self.health} de health\n")