import shutil
import pathlib

ruta_original = str(pathlib.Path().absolute()) + '/13-ManejoArchivos/01-Master/01-Archivos/archivo.txt'
ruta_nueva = str(pathlib.Path().absolute()) + '/13-ManejoArchivos/01-Master/01-Archivos/archivo_movido.txt'

""" Renombrar El Archivo """
shutil.move(ruta_original, ruta_nueva)