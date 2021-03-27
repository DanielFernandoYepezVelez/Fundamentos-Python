""" VARIABLES Y CONSTANTES EN PYTHON """

# string
texto = '¡¡¡Master En Python!!!'
texto2 = 'Conociendo La Definición De Las Variables'

# CONSTANTE
SEPARADOR = '-----------------------------------'

print(texto)
print(texto2)
print(f'{SEPARADOR}\n')

# number
numeroUno = 45.678
numeroDos = 23

print(numeroUno)
print(numeroDos)
print(f'{SEPARADOR}\n')

""" CONCATENANDO VARIABLES Y SU VISUALIZACION """
nombre = 'Daniel Fernando'
apellidos = 'Yepez Vélez'
edad = 27

print(nombre + ' ' + apellidos + ' ' + 'Tiene' + ' ' + str(edad) + ' ' + 'Años')
print(f'{nombre} {apellidos} Tienen {edad} Años')
print('{} {} Tiene {} Años'.format(nombre, apellidos, edad))
print('-----------------------------------\n')