""" nameUser = input('Ingresar Nombre De Usuario: \n')
edad = int(input('Ingresar La Edad: \n'))


def showNameUser(nameUser, edadUser):
    if(edadUser >= 18):
        print(f'Tu Nombre Es: {nameUser}')
        print(f'{nameUser} Eres Mayor De Edad')
    else:
        print(f'Tu Nombre Es: {nameUser}')
        print(f'{nameUser} NO Eres Mayor De Edad')


showNameUser(nameUser, edad) """


""" EJEMPLO PRINCIPAL(INTERESANTE)"""

def tablasMultiplicar(numero):
    print(f'Tabla De Multiplicar Numero: {numero}')

    for contador in range(1, 11):
        print(f'{numero} * {contador} = {numero * contador}')
    print('##############\n')

""" tablasMultiplicar(3)
tablasMultiplicar(2)
tablasMultiplicar(6) """

""" FUNCION DENTRO DE UN CICLO """
for numero in range(1, 11):
    tablasMultiplicar(numero)

# ---------------------------------------------
def informacion(nombre, puesto):
    print(f'Soy {nombre} Y Soy {puesto}')

informacion('Daniel Fernando Yepez Vélez', 'Programador')
informacion('Andres Camilo Lopera Rosales', 'Diseñador')
informacion('Rosmari Valencia Hicapie', 'Arquitecta')