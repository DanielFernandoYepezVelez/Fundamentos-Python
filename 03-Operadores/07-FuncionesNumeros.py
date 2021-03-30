SEPARADOR = '-----------------------'

def suma(a = 0, b = 0):
    print(a + b)

print('\nSuma => ')
suma(5.1, 4.9)
suma(2.999, 33)
suma(3)

print(f'{SEPARADOR}\n')

def resta(a = 0, b = 0):
    print(a - b)

print('Resta => ')
resta(12.2, .2)
resta(5, 10)
resta(5)

print(f'{SEPARADOR}\n')

def producto(a = 0, b = 0): return a * b

productoUno = producto(5, 5)
productoDos = producto(7.5, 6.12)
productoTres = producto(7)

print('Producto => ')
print(productoUno)
print(productoDos)
print(productoTres)

print(f'{SEPARADOR}\n')

""" OJO CON EL CERO!!! """
def division(a = 0, b = 0): return a / b

divisionUno = division(8, 4)
divisionDos = division(5.4, 3.4)
divisionTres = division(5, 5)

print('División => ')
print(divisionUno)
print(divisionDos)
print(divisionTres)

print(f'{SEPARADOR}\n')

def modulo(a = 0, b = 0): return a % b

moduloUno = modulo(4, 2)
moduloDos = modulo(5, 3)
moduloTres = modulo(7, 9)

print('Modulo => ')
print(moduloUno)
print(moduloDos)
print(moduloTres)