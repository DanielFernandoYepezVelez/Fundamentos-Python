dia = int(input('Ingrese Un Numero Para Calcular Un Dia De La Semana\n'))

if dia == 1:
    print('Hoy Es Lunes')
elif dia == 2:
    print('Hoy Es Martes')
elif dia == 3:
    print('Hoy Es Miercoles')
elif dia == 4:
    print('Hoy Es Jueves')
elif dia == 5:
    print('Hoy Es Viernes')
elif dia == 6 or dia == 7:
    print('Hoy Es Fin De Semana')
else:
    print('El Día Ingresado Es Desconocido')
