import os
import os.path

""" print(os.path.abspath('./13-ManejoArchivos/01-Master/01-Archivos/') + '/')
print(os.path.abspath('./') + '/13-ManejoArchivos/01-Master/01-Archivos/')
"""

""" Otra Forma De Obtener La Ruta Absoluta Y Concateno Lo Que Necesito,
Para Comprobar Si El Archivo Existe O No Existe """
rutaAbsolutaUno = os.path.abspath('./13-ManejoArchivos/01-Master/01-Archivos/') + '/archivo11.txt'
rutaAbsolutaDos = os.path.abspath('./') + '/13-ManejoArchivos/01-Master/01-Archivos/archivo.txt'

if os.path.isfile(rutaAbsolutaDos):
    print('El Archivo Existe')
else:
    print('El Archivo No Existe')