contactos = [
    {
        "name": "Daniel Fernando",
        "email": "danipez.01@gmail.com",
    },
    {
        "name": "Dante Pez",
        "email": "danipez.02@gmail.com"
    },
    {
        "name": "Camilo Rodriguez",
        "email": "danipez.03@gmail.com"
    }
]
print(contactos, '\n')

print(contactos[0]['email'])
print(contactos[1]['email'])
print(contactos[2]['email'])


print('\nLista De Contacto')
for contacto in contactos:
    print('-----------------------------')
    print(f'Nombre De Contacto: {contacto["name"]}')
    print(f'Email De Contacto: {contacto["email"]}')