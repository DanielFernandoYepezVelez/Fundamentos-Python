countNotas = 0
acNotasEstudiantes = 0
promedio = float()
notaMayor = 0
notaMenor = 5

for i in range(1,21):
    notasEstudiantes = float(input(f'Ingrese La Nota Del Estudiante #{i}: '))   

    if(notaMayor < notasEstudiantes):
        notaMayor = notasEstudiantes

    if(notasEstudiantes < notaMenor):
        notaMenor = notasEstudiantes

    acNotasEstudiantes += notasEstudiantes
    countNotas += 1
    promedio = acNotasEstudiantes / countNotas 

print('')
print(f'Promedio Grupo: {promedio}')
print(f'Nota Mas Alta: {notaMayor}')
print(f'Notas Mas baja: {notaMenor}')