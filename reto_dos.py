# Escribe un programa que reciba como parámetro “piedra”, “papel”, o “tijera” y determine si ganó el jugador 1 o el jugador 2.
# Bonus: determina que el ganador sea el jugador que gane 2 de 3 encuentros.
import os
def run():
    turnos = 0 #contador de jugadas
    jug1 = 0 #contador de victorias de cada jugador
    jug2 = 0
    while turnos < 3:
        jugador_1 = str(input('Turno Jugador 1: Escribe piedra, papel o tijera: ').lower())
        clear() #para que se borre la pantalla cada vez que un jugador escribe su elección
        jugador_2 = str(input('Turno Jugador 2: Escribe piedra, papel o tijera: ').lower())
        clear()
        if (jugador_1 == 'piedra' and jugador_2 == 'papel') or (jugador_1 == 'papel' and jugador_2 == 'tijera') or (jugador_1 == 'tijera' and jugador_2 == 'piedra'):
            turnos += 1
            jug2 += 1
            if jug2 == 2:
                print('Ganó Jugador 2')
                break
        elif (jugador_1 == 'papel' and jugador_2 == 'piedra') or (jugador_1 == 'tijera' and jugador_2 == 'papel') or (jugador_1 == 'piedra' and jugador_2 == 'tijera'):
            turnos += 1
            jug1 += 1
            if jug1 == 2:
                print('Ganó Jugador 1')
                break
        elif (jugador_1 == jugador_2):
            print('Iguales, repetir')
            
        else:
            print('Error, recuerda solo escribir piedra, papel o tijera')
def clear():
    os.system('cls')
            
if __name__ == '__main__':  
    run()