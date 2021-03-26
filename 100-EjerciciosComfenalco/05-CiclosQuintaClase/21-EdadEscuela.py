cantidadSalones = int(input('Ingrese la cantidad de salones: '))
acEdadAlumnos = 0
promedioEdadEscuela = 0
i = 1
j = 1

while i <= cantidadSalones:
    estudiantesPorSalon = int(input(f'Ingrese el numero de estudiantes del salon #{i}: '))

    while j <= estudiantesPorSalon:
        edad = int(input(f'Ingrese la edad del estudiante #{j}: '))
        acEdadAlumnos += edad
        j += 1

    promedioEdadAlumnos = acEdadAlumnos / estudiantesPorSalon
    print(f'\nPromedio Edad Salon #{i}: {promedioEdadAlumnos}\n')
    
    j = 1
    acEdadAlumnos = 0
    promedioEdadEscuela += promedioEdadAlumnos
    promedioEdadAlumnos = 0
    i += 1

promedioTotal = promedioEdadEscuela / cantidadSalones
print(f'\nCantidad Salones: {cantidadSalones}')
print(f'Promedio Edad Escuela: {promedioEdadEscuela}')