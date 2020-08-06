user_codigo = ''
user_password = ''

while user_codigo != '1' or user_password != '1234':
    user_codigo = str(input('Ingrese Un Numero Entero(codigo): '))
    user_password = str(input('Ingrese Un Numero Entero(Password): '))

    print('')
    if user_codigo == '1' and user_password == '1234':
        print(f'Correcto: {user_codigo}\nCorrecto: {user_password}')