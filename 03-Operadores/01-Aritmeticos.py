""" OPERADOR ASIGNACIÓN """
numeroUno = 5
numeroDos = 12
restoUno = 8
restoDos = 4

numeroUnoFlotante = 2.5
numeroDosFlotante = 5.55
restoUnoFlotante = 8.8
restoDosFlotante = 4.1

""" OPERADORES ARITMETICOS """
suma = numeroUno + numeroDos
resta = numeroDos - numeroUno
producto = numeroUno * numeroDos
division = numeroDos / numeroUno
moduloRestoImpar = numeroDos / numeroUno
moduloRestoPar = restoUno % restoDos

sumaDos = numeroUnoFlotante + numeroDosFlotante
restaDos = numeroDosFlotante - numeroUnoFlotante
productoDos = numeroUnoFlotante * numeroDosFlotante
divisionDos = numeroDosFlotante / numeroUnoFlotante
moduloRestoImparDos = numeroDosFlotante / numeroUnoFlotante
moduloRestoParDos = restoUnoFlotante % restoDosFlotante

print(f'Suma => {suma}')
print(f'Resta => {resta}')
print(f'Producto => {producto}')
print(f'Division => {division}')
print(f'Modulo / Resto => {moduloRestoImpar}')
print(f'Modulo / Resto => {moduloRestoPar}')

print('-----------------------------\n')

print(f'SumaDos => {sumaDos}')
print(f'RestaDos => {restaDos}')
print(f'ProductoDos => {productoDos}')
print(f'DivisionDos => {divisionDos}')
print(f'ModuloDos / RestoDos => {moduloRestoImparDos}')
print(f'ModuloDos / RestoDos => {moduloRestoParDos}')

print('-----------------------------\n')

""" Multiplicando La Base Por Si Misma """
print(f'Multiplicando La Base Por Si Misma {4 ** 2}')