SEPARADOR = '-------------------------------' 

cantantes = ['CantanteUno', 'CantanteDos', 'CantanteTres', 'CantanteCuatro']
lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']
numeros = [10, 6, 7, 5, 8, 1, 2, 3, 4]

# ORDENAN LOS ELEMENTOS EN ESTE CASO SON NUMEROS
print(lenguajes)
lenguajes.sort()
print(lenguajes)

print(f'{SEPARADOR}\n')

print(numeros)
numeros.sort()
print(numeros)

print(f'{SEPARADOR}\n')

# REEMPLAZAR UN ELEMENTO EXISTENTE
print(lenguajes)
lenguajes[0] = 'TypeScript'
print(lenguajes)

print(f'{SEPARADOR}\n')

# AGREGAR UN ULTIMO ELEMENTO
print(cantantes)
cantantes.append('UltimoCantante')
print(cantantes)

print(f'{SEPARADOR}\n')

# AGREGAR ELEMENTO PERO INDICANDO LA POSICIÓN
print(cantantes)
cantantes.insert(0, 'CantanteInsertado0')
print(cantantes)
cantantes.insert(3, 'CantanteInsertado3')
print(cantantes)

print(f'{SEPARADOR}\n')

# (POP) AQUI DEFINIMOS UNA POSICIÓN, ELIMINA ELEMENTO DE LA LISTA
print(cantantes)
cantantes.pop(6)
print(cantantes)

# AQUI UTILIZAMOS EL REMOVE Y PASAMOS EL NOMBRE DEL ELEMENTO
cantantes.remove('CantanteTres')
print(cantantes)

print(f'{SEPARADOR}\n')

# AQUI NO DEFINIMOS UNA POSICIÓN, POR ENDE, ELIMINARA LA ULTIMA POSICIÓN
print(lenguajes)
lenguajes.pop()
print(lenguajes)

print(f'{SEPARADOR}\n')

# AQUI UTILIZAMOS del PARA ELIMINAR UN ELEMENTO DE UNA LISTA Y PASAMOS LA POSICIÓN
print(lenguajes)
del lenguajes[1]
print(lenguajes)

print(f'{SEPARADOR}\n')

# INVERTIR UNA LISTA DE NUMEROS
print(numeros)
numeros.reverse()
print(numeros)

print(f'{SEPARADOR}\n')

# BUSCAR DENTRO DE UNA LISTA(ARRAY)
boolean = 'CantanteUno' in cantantes
print(boolean)

print(f'{SEPARADOR}\n')

# LONGITUD DE UNA LISTA
print(len(numeros))
print(len(cantantes))

print(f'{SEPARADOR}\n')

# NUMERO DE VECES QUE APARECE UN ELEMENTO EN UNA LISTA
print(numeros.count(3))
print(cantantes.count('CantanteUno'))

print(f'{SEPARADOR}\n')

# OBTENER EL INDICE DE UN ELEMENTO DENTRO DE UNA LISTA
print(numeros.index(1))
print(cantantes.index('CantanteUno'))

print(f'{SEPARADOR}\n')

# UNIR DOS LISTAS
print(cantantes)
cantantes.extend(numeros)
print(cantantes)

print(f'{SEPARADOR}\n')