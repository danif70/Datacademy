# Para este reto final juguemos con números. En tu programa pide al usuario ingresar 3 números: un límite inferior, un límite superior y uno de comparación.
# Si tu número de comparación se encuentra en el rango de los dos límites, imprímelo en pantalla.
# En caso de estar por debajo del inferior o arriba del superior, también muéstralo en pantalla y pide ingresar otro número para repetir el proceso.


def run():
    print('''Probemos si la computadora compara números correctamente''')
    numero_inf = int(input('Escribe tu número inferior:  '))
    numero_sup = int(input('Escribe tu número superior: '))
    tercer_numero = int(input('Escribe el número a comparar: '))
    comparacion(numero_inf, numero_sup, tercer_numero)
    
def comparacion(numero_inf, numero_sup, tercer_numero):
    if tercer_numero > numero_inf and tercer_numero < numero_sup:
        print(f'El tercer número {tercer_numero} está entre {numero_inf} y entre {numero_sup}')
    else:
        print(f'{tercer_numero} no está entre los números dados')
        tercer_numero = int(input('Escribe otro número a comparar: '))
        comparacion(numero_inf, numero_sup, tercer_numero)        

if __name__ == '__main__':
    run()