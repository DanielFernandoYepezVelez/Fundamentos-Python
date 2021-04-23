""" Capturar Excepciones Y Manejar Errores En
Código Susceptible A Fallos/Errores """

try:
    nombre = input('¿Cual Es Tu Nombre?: ')

    if len(nombre) >= 1:
        nombre_usuario = 'El Nombre Es: ' + nombre

    print(nombre_usuario)
except:
    print('El Nombre Del Usuario Es Obligatorio')
else:
    print('El Codigo Se Ejecuto Correctamente')
finally:
    print('La Finalización Del try - except Siempre Se Ejecuta Al Final')