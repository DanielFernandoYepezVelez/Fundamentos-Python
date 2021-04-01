SEPARADOR = '##############################'

""" LAS LISTAS SON EQUIVALENTES A LOS ARRAYS """
peliculas = ['PeliUno', 'PeliDos', 'PeliTres']
print(f'Peliculas String => {peliculas}')

print(f'{SEPARADOR}\n')

peliculasTipos = [True, 'tipos', 1233]
print(f'Peliculas Tipos Dinamicos => {peliculasTipos}')

print(f'{SEPARADOR}\n')

lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']
print(f'Lenguajes De Programación String => {lenguajes}')

print(f'{SEPARADOR}\n')

print('-------------- OTRA FORMA DE DEFINIR LAS LISTAS(ARRAYS) ---------------\n')

""" OTRA FORMA DE DEFINIR LAS LISTAS, PERO SOLO
RECIBEN UN ARGUMENTO CON TODOS LOS VALORES INTERNOS
DE DICHA LISTA """

cantantes = list(('CantanteUno', 'CantanteDos', 'CantanteTres'))
print(cantantes)

print(f'{SEPARADOR}\n')

listTipos = list((344, 'ListasTipos', False))
print(listTipos)