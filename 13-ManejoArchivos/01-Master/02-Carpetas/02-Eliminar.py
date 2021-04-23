import os

""" Ruta Absoluta """
rutaAbsoluta = os.path.abspath('./13-ManejoArchivos/01-Master/02-Carpetas/carpetaCreada_COPY')

""" Comprobar Si Dicha Carpeta SI!! Existe """
if os.path.isdir(rutaAbsoluta):
    """ Eliminar Una Carpeta """
    os.rmdir(rutaAbsoluta)
else:
    print('La Carpeta No Existe')    