import os
import pathlib

ruta = str(pathlib.Path().absolute()) + '/13-ManejoArchivos/01-Master/01-Archivos/archivo_movido.txt'

""" Eliminar El Archivo """
os.remove(ruta)