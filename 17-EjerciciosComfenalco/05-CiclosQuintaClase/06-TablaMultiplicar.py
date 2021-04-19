numerosTabla = 0
user_number = float(input(f'Ingrese Un Numero Entero: '))

while numerosTabla <= 10:
    producto = user_number * numerosTabla
    print(f'{user_number} x {numerosTabla} = {producto}')
    numerosTabla += 1