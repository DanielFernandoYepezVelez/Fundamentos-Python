import os

""" Ruta Absoluta """
rutaAbsoluta = os.path.abspath('./13-ManejoArchivos/01-Master/02-Carpetas/carpetaCreada')

""" Comprobar Si Dicha Carpeta NO!! Existe """
if not os.path.isdir(rutaAbsoluta):
    """ Crear Carpeta """
    os.mkdir(rutaAbsoluta)
else:
    print('Ya Existe El Directorio')