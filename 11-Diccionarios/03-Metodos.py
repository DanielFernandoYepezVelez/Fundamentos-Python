SEPARADOR = '--------------------'

cancion = {
    'artista': 'Music Team',
    'nombre': 'Noche Tony',
    'lanzamiento': 2000,
    'likes': 200
}

print(cancion)
print(cancion['artista'])
print(cancion['lanzamiento'])

""" Mezclando El Objeto Con La Interpolación De Strings """
nombre = cancion['nombre']
print(f'Estoy Escuchando {nombre}')

print(f'{SEPARADOR}\n')

""" Agregar Valores Al Diccionario (Objeto) En La Ultima Posición """
cancion['playlist'] = 'Reggueton'
print(cancion)

print(f'{SEPARADOR}\n')

""" Editando Una Key Existente Al Diccionario (Objeto) """
cancion['nombre'] = 'Cancion Reemplazada'
print(cancion)

print(f'{SEPARADOR}\n')

""" Eliminar Una Key Existente Al Diccionario (Objeto) """
del cancion['lanzamiento']
print(cancion)