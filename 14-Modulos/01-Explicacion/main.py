""" Se Crea La Carpeta __pycache__ De Forma Automatica """

""" Es La Forma Como Podemos Expandir Nuestro Programa
De Forma Organizada, Limpia Y Modularizada."""

""" Importando Un Modulo Propio Con Todo En Su Interior,
Pero Referenciando El Modulo Antes. """
import moduloPrueba

""" Importando Algo En Particular Del Modulo Propio. """
from moduloPrueba2 import saludo

""" Importando Un Modulo Propio Con Todo En Su Interior,
Pero NO Referenciando El Modulo Antes. """
from moduloPrueba3 import *

print(moduloPrueba.holaMundo('Daniel'))
print(saludo('Daniel Fernando'))
print(saludando('Daniel Fernando', 'Yepez Vélez'))