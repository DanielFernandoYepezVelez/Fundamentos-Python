SEPARADOR = '--------------------'

jugador = {}
print(jugador)

print(f'{SEPARADOR}\n')

""" Para Agregar Un Nuevo Jugador Al Diccionario Vacio """
jugador['nombre'] = 'Danielito Fernandito'
jugador['puntaje'] = 0
print(jugador)

print(f'{SEPARADOR}\n')

# Incrementando El Puntaje
jugador['puntaje'] = 110
print(jugador)

print(f'{SEPARADOR}\n')

""" Acceder A Un Valor Existente En El Diccionario """
print(jugador.get('puntaje'))

print(f'{SEPARADOR}\n')

""" Acceder A Un Valor Que NO!! Existe En El Diccionario """
print(jugador.get('consola'))
print(jugador.get('consola', 'No Existe En El Diccionario')) # Mensaje Personalizado

print(f'{SEPARADOR}\n')

""" Iterar En Los Diccionarios (Objetos), Muy Similar Como Se Puede Iterar En Las Listas (Arrays)"""
for llave, valor in jugador.items():
    print(f'llave: {llave} Valor: {valor}')

print(f'{SEPARADOR}\n')

""" Eliminar De La Lista """
del jugador['nombre']
del jugador['puntaje']
print(jugador)