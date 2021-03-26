numeroAutomoviles = input('Ingrese El Número De Automoviles Que Posee: ')
acImpuestoCategoriaUno = 0
acImpuestoCategoriaDos = 0
acImpuestoCategoriaTres = 0
impuestoAutomovilUno = 0
impuestoAutomovilDos = 0
impuestoAutomovilTres = 0
i = 1

while i <= int(numeroAutomoviles):
  valorAutomovil = float(input(f'Ingrese El Valor Del Automovil #{i}: '))
  numeroCategoria = int(input(f'Ingrese La Categoria(1/2/3) Del Automovil #{i}: '))  

  if numeroCategoria == 1:
    impuestoAutomovilUno = valorAutomovil * 0.1
    print(f'\nImpuesto individual Vehiculo #{i}: {impuestoAutomovilUno} Pesos\n')
    acImpuestoCategoriaUno += impuestoAutomovilUno

  elif numeroCategoria == 2:
    impuestoAutomovilDos = valorAutomovil * 0.07
    print(f'\nImpuesto individual Vehiculo #{i}: {impuestoAutomovilDos} Pesos\n')
    acImpuestoCategoriaDos += impuestoAutomovilDos

  elif numeroCategoria == 3:
    impuestoAutomovilTres = valorAutomovil * 0.05
    print(f'\nImpuesto individual Vehiculo #{i}: {impuestoAutomovilTres} Pesos\n')
    acImpuestoCategoriaTres += impuestoAutomovilTres

  else:
    print('\nLa Categoria Ingresada No Existe, Por Ende, No Se Tendra En Cuenta El Valor Del Vehiculo Ingresado\n')

  i += 1

impuestoTotalCategorias = acImpuestoCategoriaUno + acImpuestoCategoriaDos + acImpuestoCategoriaTres
print(f'\nImpuesto Total Categoria Uno: {acImpuestoCategoriaUno} Pesos')
print(f'Impuesto Total Categoria Dos: {acImpuestoCategoriaDos} Pesos')
print(f'Impuesto Total Categoria Tres: {acImpuestoCategoriaTres} Pesos')
print(f'Impuesto Total Todas Las Categorias: {impuestoTotalCategorias} Pesos')