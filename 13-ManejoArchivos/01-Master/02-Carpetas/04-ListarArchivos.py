import os

""" Ruta Absoluta """
rutaOriginal = os.path.abspath('./13-ManejoArchivos/01-Master/02-Carpetas/carpetaCreada')

print('Listar Archivos De La Carpeta Creada: ')
contenido = os.listdir(rutaOriginal)

for archivo in contenido:
    print(f'Archivo Dentro De La Carpeta: {archivo}')