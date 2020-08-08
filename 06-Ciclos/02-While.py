contador = 1

while contador <= 5:
    print(f'El Contador Va Por El Numero {contador}')
    contador += 1
else:
    print('El Bloque Termino Correctamente\n')

""" EJEMPLO TABLA DE MULTIPLICAR """
numberUser = int(input(f'Ingrese Un Numero Para Multiplicar: \n'))
contador = 1

if numberUser < 1:
    numberUser = 1

while contador <= 10:
    print(f'{numberUser} * {contador} = {numberUser * contador}')
    contador += 1
else:
    print('Tabla Finalizada')
