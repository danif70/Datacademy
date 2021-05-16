# Esta es la forma con menos inputs que encontré para resolver el triángulo
import math
def run():
    semip = (lado_a + lado_b + lado_c)/2 #esta fórmula calcula el perímetro del triángulo entre dos porque este dato es necesario para la fórmula de Heron
    area_heron = (math.sqrt(semip*(semip - lado_a)*(semip - lado_b)*(semip - lado_c))) #esta fórmula calcula el área de cualquier tipo de triángulo
    altura = (area_heron*2)/lado_a
    print(f'El área del triángulo es {area_heron}cm2  y su altura {altura}cm') #utilizando la fórmula de área proporcionada en el reto se calcula la altura del triángulo
    tipo_de_triangulo()
    
def tipo_de_triangulo(): #comparativa entre lados para determinar el tipo de triángulo
    if lado_a == lado_b and lado_b == lado_c:
        print('El triángulo es equilátero') 
    elif (lado_a == lado_b and lado_b != lado_c) or (lado_a != lado_b and lado_b == lado_c) or (lado_a != lado_b and lado_a == lado_c):
        print('El triángulo es isóceles')
    else:
        print('El triángulo es escaleno')
    
if __name__ == '__main__':
    lado_a = int(input('Escribe la base del triángulo en cm: '))
    lado_b = int(input('Escribe el 2do lado en cm: '))
    lado_c = int(input('Escribe el 3er lado en cm: '))
    run()    
