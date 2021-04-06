ventasVendedor = int(input('Ingrese La Cantidad De Ventas Realizadas: '))

contadorVentasUno = 0
contadorVentasDos = 0
contadorVentasTres = 0
acVentaUno = 0
acVentaDos = 0
acVentasTres = 0
globalVentas = 0
iterador = 1

while iterador <= ventasVendedor:
    valorVenta = float(input(f'Ingese El Valor De la Venta #{iterador}: '))

    if valorVenta <= 10000:
        contadorVentasUno += 1
        acVentaUno += valorVenta

    elif valorVenta > 10000 and valorVenta < 20000:
        contadorVentasDos += 1
        acVentaDos += valorVenta

    else:
        contadorVentasTres += 1
        acVentasTres += valorVenta        

    iterador += 1

globalVentas += acVentaUno + acVentaDos

print(f'\nVentas Menores o iguales a 10,000: {contadorVentasUno}')
print(f'Valor Economico De Ventas Menores o iguales a 10,000: {acVentaUno} pesos')
print(f'Ventas Mayores a 10,000 y Menores a 20,000: {contadorVentasDos}')
print(f'Valor Economico De Ventas Mayores a 10,000 y Menores a 20,000: {acVentaDos} pesos')
print(f'Ventas Globales Menores a 20,000: {globalVentas} pesos')


print(f'\nVentas Mayores o iguales a 20,000: {contadorVentasTres}')
print(f'Valor Economico De Ventas Mayores o iguales a 20,000: {acVentasTres} pesos')