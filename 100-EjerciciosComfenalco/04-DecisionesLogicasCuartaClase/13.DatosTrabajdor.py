nombre = str(input('Ingrese el nombre del empleado: '))
horasT = int(input('Ingrese el numero de horas trabajadas: '))
valorH = float(input('Ingrese el valor de la hora: '))

print(' ')
if horasT <= 48:
    salarioBruto = horasT * valorH
    bonificaciones = 20000

    if valorH < 5000:
        deducciones = 10000        
    elif valorH > 5000 and valorH < 8000:
        deducciones = 20000
    elif valorH >= 8000:
        deducciones = 50000            

    salarioNeto = ((salarioBruto + bonificaciones) - deducciones)

    print(f'Salario Bruto: {salarioBruto}')
    print(f'Bonificaciones: {bonificaciones}')
    print(f'Deducciones: {deducciones}')
    print(f'Salario Neto: {salarioNeto}')
        
elif horasT >= 49 and horasT <= 58:
    salarioBruto = horasT * valorH
    bonificaciones = 50000

    if valorH < 5000:
        deducciones = 10000        
    elif valorH > 5000 and valorH < 8000:
        deducciones = 20000
    elif valorH >= 8000:
        deducciones = 50000            
    
    salarioNeto = ((salarioBruto + bonificaciones) - deducciones)

    print(f'Salario Bruto: {salarioBruto}')
    print(f'Bonificaciones: {bonificaciones}')
    print(f'Deducciones: {deducciones}')
    print(f'Salario Neto: {salarioNeto}')
    
elif horasT > 58:
    salarioBruto = horasT * valorH
    bonificaciones = 100000

    if valorH < 5000:
        deducciones = 10000        
    elif valorH > 5000 and valorH < 8000:
        deducciones = 20000
    elif valorH >= 8000:
        deducciones = 50000            
    
    salarioNeto = ((salarioBruto + bonificaciones) - deducciones)

    print(f'Salario Bruto: {salarioBruto}')
    print(f'Bonificaciones: {bonificaciones}')
    print(f'Deducciones: {deducciones}')
    print(f'Salario Neto: {salarioNeto}')
else:
    print('Error')        