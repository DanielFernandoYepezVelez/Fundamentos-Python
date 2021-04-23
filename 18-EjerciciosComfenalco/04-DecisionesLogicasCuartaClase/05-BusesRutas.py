placaBus = str(input('Ingrese La Placa Del Bus: '))
pasajerosTransportados = int(input('Ingrese Pasajeros Transportados: '))
rutaServicio = str(input('Ingrese La Ruta De Servicio A ó B: '))

print('')
if rutaServicio == 'a' or rutaServicio == 'A':
    ganaciasBus = pasajerosTransportados * 1200

    print('Ruta: ', rutaServicio)
    print(f'Ganacia Bus: {ganaciasBus}') 

elif rutaServicio == 'b' or rutaServicio == 'B':
    ganaciasBus = pasajerosTransportados * 1000

    print('Ruta: ', rutaServicio)
    print(f'Ganacia Bus: {ganaciasBus}') 

else:
    print('La letra ingresada no hace parte del ejercicio')