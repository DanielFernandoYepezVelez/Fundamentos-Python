acAhorroDiario = 1

for iterador in range(1,366):
    acAhorroDiario *= 3
    print(f'Ahorro Dia #{iterador}: {acAhorroDiario} pesos')

print(f'\nAhorro Anual: {acAhorroDiario} pesos')