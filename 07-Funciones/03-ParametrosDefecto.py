def getEmpleado(nombreEmployee, idEmployee='N/A'):
    if(idEmployee == 'N/A'):
        print(f'NOMBRE => {nombreEmployee}\n')
    else:
        print(f'NOMBRE => {nombreEmployee}')
        print(f'DNI => {idEmployee}\n')


getEmpleado('Daniel Fernando', 123233)
getEmpleado('Daniel Fernando')

# ---------------------------------------------
def informacion(nombre, puesto = 'Desconocido'):
    print(f'Soy {nombre} Y Soy {puesto}')

informacion('Daniel Fernando Yepez Vélez', 'Programador')
informacion('Andres Camilo Lopera Rosales', 'Diseñador')
informacion('Rosmari Valencia Hicapie')