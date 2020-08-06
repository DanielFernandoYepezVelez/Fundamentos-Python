cantidadFocos = int(input('Ingrese la cantidad del lote de focos: '))
iterador = 1
contadorVerde = 0
contadorBlanco = 0
contadorRojo = 0

while iterador <= cantidadFocos:

    colorFoco = str(input(f'Ingrese el color del foco (Verde/Blanco/Rojo) #{iterador}: '))

    if colorFoco == 'verde' or colorFoco == 'VERDE':
        contadorVerde += 1

    elif colorFoco == 'BLANCO' or colorFoco == 'blanco':
        contadorBlanco += 1

    elif colorFoco == 'rojo' or colorFoco == 'ROJO':
        contadorRojo += 1

    iterador += 1

print(f'\nCantidad De Focos Color Verde: {contadorVerde}')    
print(f'Cantidad De Focos Color Blanco: {contadorBlanco}')    
print(f'Cantidad De Focos Color Rojo: {contadorRojo}')