numeroTrabajadores = int(input('Ingrese El Numero De Empleados: '))
acSalario = 0
i = 1

while i <= numeroTrabajadores:
    nombreEmpleado = str(input(f'Ingrese El Nombre Del Empleado #{i}: '))
    horasTrabajadas = float(input(f'Ingrese Las Horas Trabajadas Por {nombreEmpleado}: '))
    sueldoEmpleado = float(input(f'Ingrese El Salario Del Empleado {nombreEmpleado}: '))

    if sueldoEmpleado >= 0 and sueldoEmpleado <= 150:
        salario = horasTrabajadas * sueldoEmpleado
        acSalario += salario

    elif sueldoEmpleado > 150 and sueldoEmpleado < 300:
        salario = horasTrabajadas * sueldoEmpleado
        acSalario += salario

    elif sueldoEmpleado > 300 and sueldoEmpleado < 450:
        salario = horasTrabajadas * sueldoEmpleado
        acSalario += salario

    elif sueldoEmpleado >= 450 and sueldoEmpleado <= 449:
        salario = horasTrabajadas * sueldoEmpleado
        acSalario += salario

    else:
        print('\nNadie Gana Más De 449 Pesos, Por Ende, Ese Sueldo Se Incluye En La Suma Total Con Un Valor De 0 Pesos\n')

    i += 1

print(f'\nLa Suma Total Del Salario De Los {numeroTrabajadores} Trabajadores Es: {acSalario}')