""" Ejercicio 3.
Programa Que Compruebe Si Una Variable Esta Vacia,
En Caso Tal, Debe Agregar Un String En Minúsculas Y 
Mostrarlo En Mayúsculas """

texto = ''

if len(texto.strip()) <= 0:
    texto = 'Hola Soy Un Texto En Minúscula Convertido A Mayúscula'
    print(texto.upper())
else:
    print(f'La Variable Tiene Contenido {texto}')