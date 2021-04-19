""" Ejercicio 5.
Crear Una Lista Con El Contenido De Esta Tabla:
ACCIÓN     AVENTURA          DEPORTES
GTA        ASSINS            FIFA 21
COD        CRASH             PRO 21
PUGB       Prince Of Persia  MOTO GP 21 

Mostrar Esta Información Ordenada """

tabla = [
    {
        "categoria": "ACCIÓN",
        "juegos": ['GTA', 'CALL OF DUTY', 'PUGB']
    },
    {
        "categoria": "AVENTURA",
        "juegos": ['ASSASINS', 'CRASH BANDICOOT', 'PRINCE OF PERSIA']
    },
    {
        "categoria": "DEPORTES",
        "juegos": ['FIFA 21', 'PRO 21', 'MOTO GP 21']
    }
]

for categoriaPrincipal in tabla:
    print(f'---------------- {categoriaPrincipal["categoria"]} ------------------')
    for juego in categoriaPrincipal["juegos"]:
        print(juego)