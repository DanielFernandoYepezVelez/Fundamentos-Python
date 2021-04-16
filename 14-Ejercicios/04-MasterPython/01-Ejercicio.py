""" Ejercicio 1.
Hacer Un Programa Que Tenga Una Lista De 8 Números
Enteros Y Haga Lo Siguiente:
- Crear Una Lista De Números.
- Recorrer La Lista Y Mostrarla.
- Hacer Función Que Recorra Una De Cualquier Cosa Y Devuelva Un String.
- Ordenarla Y Mostrarla.
- Mostrar Su Longitud.
- Buscar Algún Elemento (Que El Usuario Pida Por Teclado).
"""

SEPARADOR = '--------------------------------'

# Crear Una Lista De Números Y De Otros Tipos De Datos
numeros = [10, 13, 17, 23, 28, 41, 55, 12, 100, 67, 37]
nombres = ['Daniel', 'Fernando', 'Ana Maria', 'Rosita', 'Martina', 'Carmela', 'Andrès']

# Recorrer La Lista Y Mostrarla
print('\nMostrar Lista De Numeros: ')
for numero in numeros:
    print(f'Numero => {numero}')

print(f'{SEPARADOR}\n')

# Hacer Función Que Recorra Una Lista Reutilizable Y Devuelva Un String
print('Mostrar Listas Reutilizables: ')
def elementos(lista):
    resultado = ""
    
    for elemento in lista:
        resultado += 'Elemento => ' + str(elemento)
        resultado += '\n'

    return resultado

print(elementos(numeros))
print(f'{SEPARADOR}')
print(elementos(nombres))

# Ordernar Las Listas Y Mostrarlas
numeros.sort()
nombres.sort()

print('\nOrdenar Las Listas Y Mostrarlas: ')
print(elementos(numeros))
print(f'{SEPARADOR}')
print(elementos(nombres))

# Mostrar Longitud De Las Listas
print('\nMostrar Longitud De Las Listas: ')
print(f'Longitud Lista Números: {len(numeros)}')
print(f'{SEPARADOR}')
print(f'Longitud Lista Nombres: {len(nombres)}')

# El Profesor Debe Mejorar Su Lógica
# Buscar Algún Elemento (Que El Usuario Pida Por Teclado).
print('\nBuscar Dentro De Las Listas: ')

busqueda = int(input('Ingresa El Número A Buscar: '))
comprobar = isinstance(busqueda, int)

while not comprobar or busqueda <= 0:
    busqueda = int(input('Ingresa El Número A Buscar: '))
else:
    print(f'Has Ingresado El Número {busqueda}')

search = numeros.index(busqueda)
print(f'El Indice Del Número Buscado En La Lista Es: {search}')