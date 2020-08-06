tipoEmpleado = str(input('Ingrese Si ElEmpleado es Temporal o Fijo: '))

print('')
if tipoEmpleado == 'fijo' or tipoEmpleado == 'FIJO':
    nombreEmpleado = str(input('Ingrese El Nombre: '))
    horasT = int(input('Horas Trabajas: '))
    salarioH = float(input('Salario Hora: '))
    deducciones = float(input('Total Deducciones Empleado: '))
    bonificaciones = float(input('Total Bonificaciones Empleado: '))

# Operaciones
    salarioNeto = ((horasT * salarioH) + bonificaciones) - deducciones

    print('')
    print(f'Tipo Empleado: {tipoEmpleado}')
    print(f'Nombre Empleado: {nombreEmpleado}')
    print(f'Salario Empleado: {salarioNeto}')

elif tipoEmpleado == 'temporal' or tipoEmpleado == 'TEMPORAL':
    nombreEmpleado = str(input('Ingrese El Nombre: '))
    horasT = int(input('Horas Trabajadas: '))
    salarioH = 6000

# Operaciones
    salarioNeto = horasT * salarioH

    print('')
    print(f'Tipo Empleado: {tipoEmpleado}')
    print(f'Nombre Empleado: {nombreEmpleado}')
    print(f'Salario Empleado: {salarioNeto}')

else:
    print('Tipo De Empleado Es Erroneo') 