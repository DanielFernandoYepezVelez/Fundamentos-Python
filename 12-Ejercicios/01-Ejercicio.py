""" 
Hacer una lista que tenga ocho numeros enteros
y haga lo siguiente: 
- Recorrer Una Lista Y Mostrarla
- Ordenarla Y Mostrarla
- Mostrarla Su Longitud
- Buscar Algun Elemento(QUE EL USUARIO PIDA POR TECLADO)
"""
# 1.
enteros = [1, 8, 2, 7, 3, 6, 4, 5]
print('-----------------------------')
print(enteros)

print('Lista Númerica')
for entero in enteros:
    print('>>>', entero)

# 2.
enteros.sort()
print('-----------------------------')
print(enteros)
