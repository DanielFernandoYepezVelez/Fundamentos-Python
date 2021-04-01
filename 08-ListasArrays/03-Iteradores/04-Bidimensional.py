personas = [
    [
        'Daniel Fernando',
        'dani@gmail.com'
    ],
    [
        'Juan Manuel',
        'fernando@gmail'
    ],
    [
        'Rosalva Ramirez',
        'carla@gmail.com'
    ]
]

print(f'{personas}\n')

print(f'{personas[0][0]} -- {personas[0][1]}')
print(f'{personas[1][0]} -- {personas[1][1]}')
print(f'{personas[2][0]} -- {personas[2][1]}\n')

for contador in range(0, personas.__len__()):
    print(f'{personas[contador]}')

""" ITERAR SOBRE EL ARRAY PRINCIPAL """
""" POSTERIORMENTE ITERAR SOBRE EL VALOR DEL RESULTADO DE LA ITERACIÓN PRINCIPAL """
print('\n')
for MatrizPersonas in personas:
    for persona in MatrizPersonas:
        print(f'{persona}')
    print('\n')

for MatrizPersonas in personas:
    for persona in MatrizPersonas:
        if(MatrizPersonas.index(persona) == 0):
            print(f'Nombre = {persona}')
        else:
            print(f'Email = {persona}')
