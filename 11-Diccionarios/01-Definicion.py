""" Es Un Tipo De Dato Que Almacena Un Conjunto
De Datos, En Formato Clave - Valor.
Es Similar A Un Objeto JSON """

user = {
    "name": "Daniel Fernando",
    "lastName": "Yepez Velez",
    "edad": 40,
    "activate": True
}

print(user)
print(user['activate'])
print(user['edad'])
print(type(user))

print('-------------\n')

cancion = {
    'artista': 'Music Team',
    'nombre': 'Noche Tony',
    'lanzamiento': 2000,
    'likes': 200
}

print(cancion)
print(cancion['artista'])
print(cancion['lanzamiento'])