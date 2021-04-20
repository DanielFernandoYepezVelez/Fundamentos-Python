import shutil
import pathlib

ruta_original = str(pathlib.Path().absolute()) + '/13-ManejoArchivos/01-Master/01-Archivos/archivo.txt'
ruta_nueva = str(pathlib.Path().absolute()) + '/13-ManejoArchivos/01-Master/01-Archivos/archivo_copy.txt'

""" Copia El Archivo Exactamente Igual """
shutil.copyfile(ruta_original, ruta_nueva)