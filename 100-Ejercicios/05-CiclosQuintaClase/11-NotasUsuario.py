acNotas = 0
countNotas = 0
continuar = 'si'
 
while (continuar != 'NO') or (continuar != 'no'):
    notas = float(input('Ingrese Una Nota: '))
    continuar = str(input('Desea Ingresar Una Nueva Nota(si/no): '))
    
    countNotas += 1
    acNotas += notas

    if(continuar == 'no') or (continuar == 'NO'):
        promedio = acNotas / countNotas
        print(f'Promedio Final: {promedio}')
        break