playlist = {}
playlist['canciones'] = []

""" FUNCIÓN PRINCIPAL """
def app():
    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input('Como Deseas Nombrar La Playlist?\n')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False

app()