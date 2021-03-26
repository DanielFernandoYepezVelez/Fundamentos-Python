for personas in range(1,4):
    user_name = str(input('Ingrese Su Nombre: '))
    user_age = int(input('Ingrese Su Edad: '))

    print('')
    if(user_age < 18):
        print(f'\nNombre: {user_name}\nEdad: {user_age} Años\nSe Encontró Un Menor De Edad')
        break
    elif (user_age >= 18 and personas >=3):
        print('No Hay Ningun Menor De Edad')