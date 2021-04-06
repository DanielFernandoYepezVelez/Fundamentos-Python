def app():

    """ No Es Necesario Cerrar La Conexión Del Archivo, Es Una Función Más Nueva """
    with open('13-ManejoArchivos/archivo.txt') as archivo:
        for contenido in archivo:
            print(contenido.rstrip())

app()