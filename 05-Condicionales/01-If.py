# Condicional IF

SEPARADOR = '-----------------'

""" EJEMPLO #1 """
# color = input('¿Ingresa Color Favorito?\n')
color = 'rojo'

if color == 'rojo':
    print('Color Es Rojo')
else:
    print('Color NO Es Rojo')

print(f'{SEPARADOR}\n')

""" EJEMPLO #2 """
year = int(input('¿Ingresa En Año Estamos?\n'))
# year = 2020

if year >= 2021:
    print(f'Estamos De 2021 En Adelante')
else:
    print(f'Es Un Año Anterior A 2021')

print(f'{SEPARADOR}\n')

""" EJEMPLO #3 """
lenguaje = 'python';

if not lenguaje == 'python':
    print(f'Excelente Decisión Aprendiendo {lenguaje}')
else:
    print(f'Mala Decisión NO! Aprendiendo {lenguaje}')

print(f'{SEPARADOR}\n')

""" EJEMPLO #4 """
peliculas = ['PeliUno', 'PeliDos', 'PeliTres']

if 'PeliUno' in peliculas:
    print('La Pelicula Uno Si Existe En La Lista')