codigoArticulo = int(input('Ingrese El Codigo Del Articulo: '))
cantidadArticulos = int(input('Ingrese La Cantidad De Articulos: '))
valorArticulo = float(input('Ingrese Del Articulo Comprado: '))

if cantidadArticulos >= 50:
    valorCompra = cantidadArticulos * valorArticulo
    descuento = valorCompra * 0.1
    totalPago = valorCompra - descuento
else:
    descuento = 0
    totalPago = cantidadArticulos * valorArticulo

print('')        
print(f'Codigo Articulo: {codigoArticulo}')
print(f'Valor Descuento: {descuento} Pesos')
print(f'Valor Compra Total: {totalPago} Pesos')