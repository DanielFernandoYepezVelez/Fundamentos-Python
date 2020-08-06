nombreUno = str(input('Ingrese El Nombre: '))
edadUno = int(input('Ingrese La Edad: '))

nombreDos = str(input('Ingrese El Nombre: '))
edadDos = int(input('Ingrese La Edad: '))

if edadUno > edadDos:
    print(f'Hermano Mayor es: {nombreUno}')
elif edadDos > edadUno:
    print(f'Hermano Mayor es: {nombreDos}')
else:
    print(f'Los Hermanos Tienen La Misma Edad.')