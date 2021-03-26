numeroUno = float(input('Ingrese Un Numero Uno: '))
numeroDos = float(input('Ingrese Un Numero Dos: '))
numeroTres = float(input('Ingrese Un Numero Tres: '))

print('')
if numeroUno > numeroDos and numeroUno > numeroTres:
    print(f'El Numero Mayor Es: {numeroUno}')
elif numeroDos > numeroUno and numeroDos > numeroTres:
    print(f'El Numero Mayor Es: {numeroDos}')
elif numeroTres > numeroUno and numeroTres > numeroDos:
    print(f'El Numero Mayor Es: {numeroTres}')  
else:
    print('Todos Los Numeros Son Iguales')      