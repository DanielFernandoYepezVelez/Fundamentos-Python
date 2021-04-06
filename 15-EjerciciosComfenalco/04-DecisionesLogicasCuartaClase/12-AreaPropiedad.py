areaPropiedad = float(input('Ingrese el area que ocupa la propiedad: '))
valorMetroCuadrado = float(input('Ingrese el costo del metro cuadrado: '))
pagoInicial = int(input('Ingrese la forma de pago 1 ó 2: '))

print('')
if pagoInicial == 1:
    precioVenta = areaPropiedad * valorMetroCuadrado
    valorCuotaInical = precioVenta * 0.2
    descuento = valorCuotaInical * 0.1
    cuotaInicialFinal = valorCuotaInical - descuento

    print(f'Precio Venta: {precioVenta}')    
    print(f'Valor Cuota Inicial: {cuotaInicialFinal}')

elif pagoInicial == 2:
    precioVenta = areaPropiedad * valorMetroCuadrado
    valorCuotaInical = precioVenta * 0.2
    recargo = valorCuotaInical * 0.08
    cuotaInicialFinal = valorCuotaInical + recargo
    
    print(f'Precio Venta: {precioVenta}')    
    print(f'Valor Cuota Inicial: {cuotaInicialFinal}')

else:
    print('Error En La Forma De Pago')