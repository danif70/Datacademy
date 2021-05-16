# Escribe un programa donde apliques las diferentes fórmulas matemáticas para calcular el volumen de un cilindro.
# Recuerda que la base del cilindro es un círculo y necesitarás calcular su área. Aplica las fórmulas en tu programa recibiendo datos como altura y radio.
# Bonus: agrega otras figuras geométricas a tu programa y que el usuario pueda escoger cuál calcular.
def run():
    print(
        ''' Este es un programa 
        para calcular el volúmen de 
    cuerpos geométricos, bienvenido/a''')
    cuerpo = int(input('''Escoge cuál cuerpo geométrico deseas calcular su volumen: 
(Cubo = 1), (Ortoedro = 2), (Pirámide = 3), (Cilindro = 4), (Cono = 5), (Esfera = 6): '''))
    if cuerpo == 1:
        lado = float(input('Por favor escribe la medida de uno de los lados del cubo en cm, si tiene decimales usa punto para separar decimales de enteros: '))
        volumen = lado**3
        print(f'El volúmen del cubo es {volumen} cms3.')
    elif cuerpo == 2:
        lado_a= float(input('Por favor escribe la medida del lado más corto de la base del ortoedro en cm, si tiene decimales usa punto para separar decimales de enteros: '))
        lado_b= float(input('Por favor escribe la medida del lado más largo del ortoedro en cm, si tiene decimales usa punto para separar decimales de enteros: '))
        altura_ortoedro= float(input('Por favor escribe la medida de la altura del ortoedro en cm, si tiene decimales usa punto para separar decimales de enteros: '))
        volumen_ortoedro = lado_a*lado_b*altura_ortoedro
        print(f'El volumen del ortoedro es {volumen_ortoedro} cms3.')
    elif cuerpo == 3:
        area_base = float(input('Por favor escribe el área de la base de la pirámide en cm, si tiene decimales usa punto para separar decimales de enteros'))
        altura_piramide = float(input('Por favor escribe la altura de la pirámide en cm, si tiene decimales usa punto para separar decimales de enteros'))
        volumen_piramide = area_base*altura_piramide/3
        print(f'El volumen de la pirámide es {volumen_piramide} cms3.')
    elif cuerpo == 4:
        diametro_base = int(input('Por favor escribe la medida del diámetro del cilindro en cm, si tiene decimales usa punto para separar decimales de enteros: '))
        altura_cilindro = int(input('Por favor escribe la medida de la altura del cilindro en cm, si tiene decimales usa punto para separar decimales de enteros: '))
        radio_cilindro= diametro_base/2
        volumen_cilindro = 3.14 * (radio_cilindro**2)*altura_cilindro
        print(f'El volumen del cilindro es {volumen_cilindro} cms3.')
    elif cuerpo == 5:
        diametro_base = int(input('Por favor escribe la medida del diámetro del cono en cm, si tiene decimales usa punto para separar decimales de enteros: '))
        altura_cono = int(input('Por favor escribe la medida de la altura del cono en cm, si tiene decimales usa punto para separar decimales de enteros: '))
        radio_cono= diametro_base/2
        volumen_cono = (3.14 * (radio_cono**2)*altura_cono)/3
        print(f'El volumen del cono es {volumen_cono} cms3.')
    elif cuerpo == 6:
        diametro_esfera = int(input('Por favor escribe la medida del diámetro de la esfera en cm, si tiene decimales usa punto para separar decimales de enteros: '))
        radio_esfera= diametro_esfera/2
        volumen_esfera = 4/3*(3.14)* (radio_esfera**3)
        print(f'El volumen de la esfera es {volumen_esfera} cms3.')
    else:
        print('Error, escoje entre las opciones dadas')
                
if __name__ == '__main__':
    run()