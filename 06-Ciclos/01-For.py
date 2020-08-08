contador = 0
resultado = 0

for contador in range(0, 10):
    print(f'Voy Por El Numero {contador}')
    resultado += contador

print(f'El Resultado Acumulativo Es: {resultado}\n')

print('##### TABLAS MULTIPLICAR ######')
numberUser = int(input('Ingresar Un Numero: \n'))

if(numberUser < 1):
    numberUser = 1

print(f'Tabla De Multiplicar Del Numero: {numberUser}')

""" INTERESANTE Y EXTRAÑO LA PARTE DEL ELSE AL FINALIZAR EL CICLO """
for i in range(0, 11):

    if numberUser == 45:
        print('El Numero Ingresado Es Prohibido')
        break

    print(f'{numberUser} * {i} = {numberUser * i}')
else:
    print('Tabla Finalizada...')
