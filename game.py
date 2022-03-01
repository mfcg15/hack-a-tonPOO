from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")
jack_sparrow = Pirate("Jack Sparrow")

jugadorSinVida = -1
jugadorGano = -1

print("Comienza el juego!\n\nLos jugadores son:\n")

michelangelo.show_stats()
jack_sparrow.show_stats()

while(jugadorSinVida!=0):
    print("Lucha!")
    print("Escoge el numero del jugador a atacar")
    print("1. Michelanglo")
    print("2. Jack Sparrow")
    numeroJugador = input("Ingrese el numero del jugador: ")

    if(numeroJugador==str(1)):
        michelangelo.attack(jack_sparrow)
        michelangelo.attack_kunai("kunai")
        jack_sparrow.show_health()
        jugadorSinVida = jack_sparrow.health
        jugadorGano = 1
    else:
        jack_sparrow.attack(michelangelo)
        jack_sparrow.attack_sword("espada")
        michelangelo.show_health()
        jugadorSinVida = michelangelo.health
        jugadorGano = 2

print("Fin del juego")
if(jugadorGano==1):
    print("El ganado es",michelangelo.name)
else:
    print("El ganador es",jack_sparrow.name)

