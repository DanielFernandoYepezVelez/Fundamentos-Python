def getEmpleado(nombreEmployee, idEmployee='N/A'):
    if(idEmployee == 'N/A'):
        print(f'NOMBRE => {nombreEmployee}\n')
    else:
        print(f'NOMBRE => {nombreEmployee}')
        print(f'DNI => {idEmployee}\n')


getEmpleado('Daniel Fernando', 123233)
getEmpleado('Daniel Fernando')
