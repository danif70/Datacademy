# escribe un programa en que el usuario indique una cantidad de millas y en pantalla se muestre el resultado convertido a kilómetros.
# Toma en cuenta que en cada milla hay 1.609344 Km
# Bonus: haz que el usuario pueda escoger entre convertir millas a kilómetros o kilómetros a millas.

def run():
    usuario = str(input('¿Desea convertir millas o Kilómetros (Escribir (m) o (k)?').lower())
    if usuario == 'm':
        millas = int(input('Escriba el número de millas a convertir: '))
        millas_convertidas = float(millas * 1.609344)
        print(f'{millas} millas equivalen a {millas_convertidas} Kms.')
    elif usuario == 'k':
        kilometros = int(input('Escriba el número de kilómetros a convertir: '))
        kilometros_convertidos = float(kilometros * 0.621371)
        print(f'{kilometros} Kms equivales a {kilometros_convertidos} millas')
    else:
        print('Opción incorrecta')   
if __name__ == '__main__':  
    run()