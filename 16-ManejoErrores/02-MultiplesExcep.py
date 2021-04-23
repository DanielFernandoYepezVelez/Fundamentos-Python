import math

try:
    numero = int(input('Ingresa Un Número: '))
    print(f'El Cuadrado Del Número {numero} Es: {numero * numero}')
except TypeError:
    print('Convertir Las Cadenas A Enteros')
except ValueError:
    print('Solo Puedes Ingresar Número Enteros')
except Exception as e:
    print(type(e))
    print('Tenemos El Siguente Error =>', type(e).__name__)