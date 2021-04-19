placaUno = str(input('Ingrese La Placa Del Vehiculo Uno: '))
pasajerosBusUno = int(input('Ingrese Pasajeros Transportados Bus Uno: '))
pasajeBusUno = float(input('Ingrese El Valor Del Pasaje Bus Uno: '))

print('')
placaDos = str(input('Ingrese La Placa Del Vehiculo Dos: '))
pasajerosBusDos = int(input('Ingrese Pasajeros Transportados Bus Dos: '))
pasajeBusDos = float(input('Ingrese El Valor Del Pasaje Bus Dos: '))

# Operaciones
ganaciasBusUno = pasajerosBusUno * pasajeBusUno
ganaciasBusDos = pasajerosBusDos * pasajeBusDos

print('')
if ganaciasBusUno > ganaciasBusDos:    
    print(f'Mayor Ganancia => \nPlaca Bus Uno: {placaUno}')
elif ganaciasBusDos > ganaciasBusUno:
    print(f'Mayor Ganancia => \nPlaca Bus Dos: {placaDos}')
else:
    print(f'Los Buses Tienen Ganacias Iguales')    