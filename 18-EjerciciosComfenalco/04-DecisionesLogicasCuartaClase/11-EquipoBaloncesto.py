nombreAtleta = str(input('Ingrese El Nombre Del Atleta: '))
genero = str(input('Ingrese El Genero M ó F: '))

print('')
if genero == 'M' or genero == 'm' or genero == 'masculino' or genero == 'MASCULINO':
    edad = int(input('Ingrese La Edad: '))
    estatura = float(input('Ingrese La Estatura: '))
    peso = float(input('Ingrese El Peso: '))

    if edad >= 18 and estatura > 1.70 and peso < 75:
        print(f'{nombreAtleta} Eres Apto Para El Equipo De Baloncesto')
    else:
        print(f'{nombreAtleta} NO Eres Apto Para El Equipo De Baloncesto')    

elif genero == 'F' or genero == 'f' or genero == 'femenino' or genero == 'FEMENINO':
    edad = int(input('Ingrese La Edad: '))
    estatura = float(input('Ingrese La Estatura: '))
    peso = float(input('Ingrese El Peso: '))

    if edad > 16 and estatura >= 1.70 and peso <= 60:
        print(f'{nombreAtleta} Eres Apta Para El Equipo De Baloncesto')
    else:
        print(f'{nombreAtleta} NO Eres Apta Para El Equipo De Baloncesto') 

else:
    print('El genero Ingresado Es Erroneo')