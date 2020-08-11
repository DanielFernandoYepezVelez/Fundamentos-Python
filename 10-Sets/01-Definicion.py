""" SET: Es Un Tipo De DATO Para Una Colleción De Valores, Pero
No Tienen Ni Orden, Ni Indice """

personas = {
    'Daniel',
    'Fernando',
    'Andres'
}

print(type(personas))
print(personas)
personas.remove('Daniel')
personas.add('Nuevo Integrante')
print(personas)
