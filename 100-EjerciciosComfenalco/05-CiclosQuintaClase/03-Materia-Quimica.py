acNotasQuimica = 0

for notaQuimica in range(1,8):
    notaEstudiante = float(input(f'Ingrese la nota #{notaQuimica}: '))
    acNotasQuimica += notaEstudiante

promedio = acNotasQuimica / 7
print('Promedio Estudiante: ', promedio)