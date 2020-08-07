""" IF ANIDADOS """
edad = int(input('Ingrese La Edad: \n'))

if edad >= 18:
    print('Eres Mayor De Edad')
    continente = input('\nIngrese Continente Origen:\n')

    if continente == 'europa':
        print(f'Eres De Europa')
        ciudad = input('\nIngresa Ciudad De Origen: \n')

        print(
            f'Tu Edad Es De \"{edad}\" Años, Contienente De Origen Es \"{continente}\" Y Ciudad De Origen Es \"{ciudad}\"')
    else:
        print('No Eres De Europa')
else:
    print('No Eres Mayor De Edad')
