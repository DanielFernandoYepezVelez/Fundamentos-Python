numeroHamburguesas = int(input('Cantidad De Hamburguesas Que Va a Comprar: '))
pagoTarjeta = str(input('Va a pagar con tarjeta de credito (si/no): '))

acValorH = 0
sobreCargo = 0
i = 1

for j in range(1, (numeroHamburguesas+1)):
    tipoHamburguesa = input(f'Ingrese El Tipo De Hamburguesa(S/D/T) #{j}: ')

    if(tipoHamburguesa == 'S' or tipoHamburguesa == 's'):
        acValorH += 20

    elif(tipoHamburguesa == 'D' or tipoHamburguesa == 'd'):
        acValorH += 25

    elif (tipoHamburguesa == 'T' or tipoHamburguesa == 't'):
        acValorH += 28
    
    if(pagoTarjeta == 'si' or pagoTarjeta == 'SI' and j == numeroHamburguesas):        
        sobreCargo = acValorH * 0.05   

    totalPago = acValorH + sobreCargo

print(f'\nCantidad Hamburguesas: {numeroHamburguesas}\nCompra Sin Recargo: {acValorH} pesos\nPaga Con Tarjeta: {pagoTarjeta}\nValor SobreCargo: {sobreCargo} pesos\nCompra Con Recargo: {totalPago} pesos')