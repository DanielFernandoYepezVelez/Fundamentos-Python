animales = []

# Agregando Elementos A La Lista
for contador in range(1, 11):
    animales.append(f'Elemento #{contador}')

# Iterando La Lista Completa
print('############# LISTA COMPLETA #################')
for i in range(0, animales.__len__()):
    print(f'{i+1}. {animales[i]}')
