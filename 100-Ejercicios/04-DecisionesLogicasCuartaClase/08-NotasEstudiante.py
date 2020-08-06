nombreEstudiante = str(input('Ingrese El Nombre Del Estudiante: '))
notaUno = float(input('Ingrese la nota #1: '))
notaDos = float(input('Ingrese la nota #2: '))
notaTres = float(input('Ingrese la nota #3: '))
notaCuatro = float(input('Ingrese la nota #4: '))

promedioEstudiante = ((notaUno + notaDos + notaTres + notaCuatro) / 4)

print('')
if promedioEstudiante >= 3:
    print('Felicitaciones GANASTE')
else:
    print('Desafortunamente PIERDES, pero ANIMO')