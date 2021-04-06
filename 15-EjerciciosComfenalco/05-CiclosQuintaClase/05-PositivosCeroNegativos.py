contadorNumerosCero = 0
contadorNumerosPositivos = 0
contadorNumerosNegativos = 0

for numeros in range(1,11):
    user_number = float(input(f'Ingrese Un Numero #{numeros}: '))

    if(user_number == 0):
        contadorNumerosCero += 1
    elif(user_number > 0):
        contadorNumerosPositivos += 1
    else:
        contadorNumerosNegativos += 1

print('')
print(f'Cantidad Numeros Positivos: {contadorNumerosPositivos} \nCantidad Numeros Negativos: {contadorNumerosNegativos} \nCantidad Numeros Ceros: {contadorNumerosCero}')