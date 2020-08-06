edad = int(input('Ingrese La Edad: '))

if edad < 10:
    print('Eres Un Niño')
elif edad > 10 and edad <= 14:
    print('Eres Un Preadolescente')    
elif edad >= 15 and edad <=18:
    print('Eres Un Adolescente')     
elif edad >= 19 and edad <= 50:
    print('Eres Un Adulto')    
elif edad > 50:
    print('Eres Un Adulto Mayor')
else:
    print('Datos Erroneos')