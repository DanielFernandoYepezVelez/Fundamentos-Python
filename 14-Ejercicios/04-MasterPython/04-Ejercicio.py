""" Ejercicio 4.
Crear Un Script Que Tenga Cuatro Variables, Una Lista, Un String
Un Entero Y Un Booleano Y Que Imprima Un Mensaje Según El Tipo
De Dato De Cada Variable. Usar Funciones. """

mi_lista = ['Hola Mundo', 77]
titulo = 'Master En Python'
numero = 100
verdadero = True

def traducirTipo(tipo):
    result = None

    if tipo == list:
        result = 'LISTA'
    elif tipo == str:
        result = 'CADENA DE TEXTO'
    elif tipo == int:
        result = 'NÚMERO ENTERO'
    elif tipo == bool:
        result = 'BOOLEANO'
    else:
        result = 'EL TIPO DE DATO ES DESCONOCIDO'

    return result    

def comprobarTipado(dato, tipo):
    test = isinstance(dato, tipo)
    result = ''

    if test:
        result = f'Este Dato Es Del Tipo {traducirTipo(tipo)}'
    else:
        result = 'El Tipo De Dato No Coincide'

    return result

print(comprobarTipado(mi_lista, list))
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, int))
print(comprobarTipado(verdadero, bool))