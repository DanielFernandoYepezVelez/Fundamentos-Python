user_number = int(input('Ingrese Un Numero Entero POSITIVO Para Obtener El Factorial: '))
factorial = 1

if user_number != 0 or user_number < 0:
  for numero in range(1,(user_number+1)):
      factorial *= numero
  print(f'Numero Factorial Del #{user_number} Es: {factorial}')

else:
  print('El Valor ingresado debe ser un NUMERO ENTERO POSITIVO')