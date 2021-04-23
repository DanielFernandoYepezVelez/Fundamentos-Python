import os, shutil

""" Ruta Absoluta """
rutaOriginal = os.path.abspath('./13-ManejoArchivos/01-Master/02-Carpetas/carpetaCreada')
rutaNueva = os.path.abspath('./13-ManejoArchivos/01-Master/02-Carpetas/carpetaCreada_COPY')

shutil.copytree(rutaOriginal, rutaNueva)