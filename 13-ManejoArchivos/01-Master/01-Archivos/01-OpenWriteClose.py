""" Del Paquete io Importo El Modulo open """
from io import open
import pathlib

""" Abrir Archivo Con Una Ruta Absoluta Y Concatenando Su Ubucación """
ruta = str(pathlib.Path().absolute()) + '/13-ManejoArchivos/01-Master/01-Archivos/archivo.txt'

""" Observar La Ruta Absoluta Es Importante, Por Que Me Ayuda A Ubicarme """
print(ruta)

archivo = open(ruta, 'a+') # Definiendo Los Permisos

""" Escribir En El Archivo Despues De Abrirlo """
archivo.write('****** Soy Un Texto Insertado Desde Python ******\n')

""" Cerrar El Archivo """
archivo.close()

""" Leer El Contenido Del Archivo """
archivoLectura = open(ruta, 'r') # Definiendo Los Permisos
archivoLectura2 = open(ruta, 'r') # Definiendo Los Permisos

contenido = archivoLectura.read()
print('Contenido Completo =>\n', contenido)

""" Leer Contenido Linea A Linea Y Guardarlo En Una Lista """
lista = archivoLectura2.readlines()

""" Cerrar El Archivo Que Leimos """
archivoLectura.close();
print(f'Lista Linea A Linea =>\n {lista}')

print('\nManipulando El Contenido De La Lista, Paso Del Archivo Independiente A Una Lista(Arreglo) =>')
for linea in lista:
    print('- ' + linea.upper())
    print(linea.center(70))