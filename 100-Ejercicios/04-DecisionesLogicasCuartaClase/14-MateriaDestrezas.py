notaUno = float(input('Ingrese La Nota #1: '))
notaDos = float(input('Ingrese La Nota #2: '))
notaTres = float(input('Ingrese La Nota #3: '))
notaCuatro = float(input('Ingrese La Nota #4: '))

# Primer Nota menor que segunda nota
# se sustituye la primera por la segunda
if notaUno < notaDos:
    notaUno = notaDos

promedioFinal = ((notaUno + notaDos + notaTres + notaCuatro) / 4)

if promedioFinal >= 4.5:
    print('Nota Final: E')
elif promedioFinal >= 4 and promedioFinal < 4.5:
    print('Nota Final: S')
elif promedioFinal >= 3.5 and promedioFinal < 4:
    print('Nota Final: B')
elif promedioFinal >= 3 and promedioFinal < 3.5:
    print('Nota Final: A')
elif promedioFinal >= 2 and promedioFinal < 3:
    print('Nota Final: D')
else:
    print('Nota Final: I')
