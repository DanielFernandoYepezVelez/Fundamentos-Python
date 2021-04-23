""" Excepciones Personalizadas O Lanzar Excepciones """
nombre = input('Ingresa Tu Nombre: ')
edad = int(input('Ingresa Tu Edad: '))

try:
    if edad < 5 or edad > 110:
        raise ValueError('La Edad Ingresada No Es Real')
    elif len(nombre) <= 1:
        raise ValueError('El Nombre No Esta Completo')
    else:
        print(f'Bienvenido Al Master En Python')
except ValueError:
    print('OJO!! Los Datos Ingresados No Son Correctos')
except Exception as e:
    print('Existe Un Error Del Tipo => ', e)