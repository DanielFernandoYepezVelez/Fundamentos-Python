playlist = {}
playlist['canciones'] = []

""" FUNCIÓN PRINCIPAL """
def app():
    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input('¿Como Deseas Nombrar La Playlist?\n')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False
            agregar_canciones()

def agregar_canciones():
    agregar_cancion = True

    while agregar_cancion:
        nombre_playlist = playlist['nombre']
        pregunta = f'\nAgrega Canciones Para La PlayList {nombre_playlist}\n'
        pregunta += 'Escribe "X" Para Dejar De Agregar Canciones\n'

        cancion = input(f'{pregunta}')

        if cancion == 'X':
            agregar_cancion = False
            mostrar_resumen()
        else:
            playlist['canciones'].append(cancion)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']

    print(f'\nPlayList => {nombre_playlist}')
    print('Canciones: ')

    for cancion in playlist['canciones']:
        print(f'- {cancion}')

app()