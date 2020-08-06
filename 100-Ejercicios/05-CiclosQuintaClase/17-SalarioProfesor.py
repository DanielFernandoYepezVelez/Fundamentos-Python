salarioInicial = 1500
acSalario = 0

for i in range(1,7):
    incremento = salarioInicial * 0.1
    salarioAnual = salarioInicial + incremento
    acSalario += salarioAnual

salarioTotal = acSalario 

print(f'Valor Incremento: {incremento} Pesos')
print(f'Salario Anual: {salarioAnual} Pesos')
print(f'Salario Total: {salarioTotal} Pesos')