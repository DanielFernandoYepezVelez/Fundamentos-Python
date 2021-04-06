sumaNumerica = 0
user_number = int(input('Ingrese Un Numero X: '))

for i in range(1, (user_number + 1)):
    sumaNumerica += i

print(f'Suma Comprendida entre el numero 1 y el numero del usuario que fue {user_number} es:',sumaNumerica)