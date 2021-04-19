""" Ejercicio 2.
Escribir Un Programa Que Añada Valores A Una Lista
Mientras Que Su Longitud Sea Menor A 120 Y Luego
Mostrar La Lista. Plus: Usar While Y For.
"""

coleccionFor = []
coleccionWhile = []

for index in range(0, 120):
    coleccionFor.append(f'Elemento #{index+1}')

print(coleccionFor)
print('Especificando La Posición => ' + coleccionFor[115])

print('\n ---------------- Mismo Ejercicio Con El White ------------------\n')

x = 0;

while x < 120:
    coleccionWhile.append(f'Elemento #{x+1}')
    x += 1

print(coleccionWhile)