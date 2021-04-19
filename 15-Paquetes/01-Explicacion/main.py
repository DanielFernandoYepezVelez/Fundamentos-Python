""" Un Paquete Es Un Conjunto De Modulos.
Podemos LLamar Los Paquetes Completos.
Podemos LLamar Los Paquetes E Importar Un Modulo En Particular.
Se Pueden Instalar Con npm O pip """

""" Importando Modulos Propios Desde Un Paquete """
from paquetePrueba import moduloPrueba1
from paquetePrueba import moduloPrueba2

""" También Es Válido Por Que Vienen Del Mismo Paquete """
# from paquetePrueba import moduloPrueba1, moduloPrueba2

print('PROBANDO PAQUETES: ')
moduloPrueba1.probando()
moduloPrueba2.nombreCompleto('Daniel Fernando', 'Yepez Vélez')