nombreUno = str(input('Ingrese El Nombre Empleado Uno: '))
salarioUno = float(input('Ingrese El Salario Del Empleado Uno: '))
deduccionesUno = float(input('Ingrese Las Deducciones Del Empleado Uno: '))
bonificacionesUno = float(input('Ingrese Las Bonificaciones Del Empleado Uno: '))

print('')
nombreDos = str(input('Ingrese El Nombre Empleado Dos: '))
salarioDos = float(input('Ingrese El Salario Del Empleado Dos: '))
deduccionesDos = float(input('Ingrese Las Deducciones Del Empleado Dos: '))
bonificacionesDos = float(input('Ingrese Las Bonificaciones Del Empleado Dos: '))

# Operaciones
salarioNetoUno = (salarioUno + bonificacionesUno) - deduccionesUno
salarioNetoDos = (salarioDos + bonificacionesDos) - deduccionesDos

print('')
if salarioNetoUno > salarioNetoDos:
    print(f'El Salario Mayor Lo Tiene {nombreUno}')
elif salarioNetoDos > salarioNetoUno:
    print(f'El Salario Mayor Lo Tiene {nombreDos}')
else:
    print(f'El Salario De {nombreUno} Y De {nombreDos} Es Igual')