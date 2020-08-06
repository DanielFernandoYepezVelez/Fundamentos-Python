user_number = int()
count_user_number = 0
ac_user_number = 0

print('Ingrese -1 Si Desea Terminar el programa')
while (user_number != (-1)):
    user_number = int(input('Ingrese El Numero: '))
    
    if user_number != (-1):
        count_user_number += 1
        ac_user_number += user_number
        promedio_number = ac_user_number / count_user_number

print(' ')
print(f'Cantidad Numeros: {count_user_number}')
print(f'Suma Numeros: {ac_user_number}')
print(f'Promedio Numeros: {promedio_number}')