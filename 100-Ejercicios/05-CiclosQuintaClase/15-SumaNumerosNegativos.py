sumaNumerosNegativos = 0

for i in range(1,5):
    user_number = float(input('Ingrese Un numero para ejecutar la suma(Solo Negativos): '))

    if user_number < 0:
        sumaNumerosNegativos += user_number

print(f'Suma Numeros Negativos: {sumaNumerosNegativos}')        