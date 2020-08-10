""" LAS LISTAS SON TIPOS DE ARRAYS """
peliculas = ['PeliUno', 'PeliDos', 'PeliTres']
print(peliculas)
print(peliculas[0])
print(peliculas[1])
print(peliculas[2])
print('##############################\n')

peliculasTipos = [True, 'tipos', 1233]
print(peliculasTipos)
print(peliculasTipos[0])
print(peliculasTipos[1])
print(peliculasTipos[2])
print('##############################\n')

""" OTRA FORMA DE DEFINIR LAS LISTAS, PERO SOLO
RECIBEN UN ARGUMENTO CON TODOS LOS VALORES INTERNOS
DE DICHA LISTA """
cantantes = list(('CantanteUno', 'CantanteDos', 'CantanteTres'))
print(cantantes)
print(cantantes[0])
print(cantantes[1])
print(cantantes[2])
print('##############################\n')

listTipos = list((344, 'ListasTipos', False))
print(listTipos)
print(listTipos[0])
print(listTipos[1])
print(listTipos[2])
print('##############################\n')

print('########## INDICES NEGATIVOS ##############')
animales = ['AnimalUno', 'AnimalDos', 'AnimalTres']
print(animales)
print(animales[-1])
print(animales[-2])
print(animales[-3])

print('\n########## SEGMENTOS DE LA LISTA O SUBLISTAS ##############')
ciudades = ['CiudadUno', 'CiudadDos', 'CiudadTres', ]
print(ciudades)
print(ciudades[0:1])
print(ciudades[1:2])
print(ciudades[2:3])
print('-----------------------------------')
print(ciudades[0:1])
print(ciudades[0:2])
print(ciudades[0:3])
print('-----------------------------------')
print(ciudades[0:])
print(ciudades[2:])
print(ciudades[3:])
