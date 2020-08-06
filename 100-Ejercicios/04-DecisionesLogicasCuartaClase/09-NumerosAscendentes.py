numeroUno = float(input('Ingrese El #1: '))
numeroDos = float(input('Ingrese El #2: '))
numeroTres = float(input('Ingrese El #3: '))

print('')
if numeroUno > numeroDos and numeroUno > numeroTres and numeroDos > numeroTres:
    print(f'Orden Ascendente: {numeroTres}, {numeroDos}, {numeroUno}')

elif numeroUno > numeroDos and numeroUno > numeroTres and numeroTres > numeroDos:
    print(f'Orden Ascendente: {numeroDos}, {numeroTres}, {numeroUno}')

elif numeroDos > numeroUno and numeroDos > numeroTres and numeroUno > numeroTres:
    print(f'Orden Ascendente: {numeroTres}, {numeroUno}, {numeroUno}') 

elif numeroDos > numeroUno and numeroDos > numeroTres and numeroTres > numeroUno:
    print(f'Orden Ascendente: {numeroUno}, {numeroTres}, {numeroUno}') 

elif numeroTres > numeroUno and numeroTres > numeroDos and numeroDos > numeroUno:
    print(f'Orden Ascendente: {numeroUno}, {numeroDos}, {numeroTres}') 

elif numeroTres > numeroUno and numeroTres > numeroDos and numeroUno > numeroDos:
    print(f'Orden Ascendente: {numeroDos}, {numeroUno}, {numeroTres}') 