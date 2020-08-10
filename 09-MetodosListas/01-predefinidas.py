cantantes = ['CantanteUno', 'CantanteDos', 'CantanteTres', 'CantanteCuatro']
numeros = [10, 6, 7, 5, 8, 1, 2, 3, 4]

# ORDENAN LOS NUMEROS
print(numeros)
numeros.sort()
print(numeros)
print('-------------------------------\n')

# AGREGAR UN ULTIMO ELEMENTO
print(cantantes)
cantantes.append('UltimoCantante')
print(cantantes)
print('-------------------------------\n')

# AGREGAR ELEMENTO PERO INDICANDO LA POSICIÓN
print(cantantes)
cantantes.insert(0, 'CantanteInsertado0')
print(cantantes)
cantantes.insert(3, 'CantanteInsertado3')
print(cantantes)
print('-------------------------------\n')

# ELIMINAR ELEMENTOS DE UNA LISTA
print(cantantes)
cantantes.pop(6)
print(cantantes)
cantantes.remove('CantanteTres')
print(cantantes)
print('-------------------------------\n')

# INVERTIR UNA LISTA DE NUMEROS
print(numeros)
numeros.reverse()
print(numeros)
print('-------------------------------\n')

# BUSCAR DENTRO DE UNA LISTA(ARRAY)
boolean = 'CantanteUno' in cantantes
print(boolean)
print('-------------------------------\n')

# LONGITUD DE UNA LISTA
print(len(numeros))
print(len(cantantes))
print('-------------------------------\n')

# NUMERO DE VECES QUE APARECE UN ELEMENTO EN UNA LISTA
print(numeros.count(3))
print(cantantes.count('CantanteUno'))
print('-------------------------------\n')

# OBTENER EL INDICE DE UN ELEMENTO DENTRO DE UNA LISTA
print(numeros.index(1))
print(cantantes.index('CantanteUno'))
print('-------------------------------\n')

# UNIR DOS LISTAS
print(cantantes)
cantantes.extend(numeros)
print(cantantes)
print('-------------------------------\n')
