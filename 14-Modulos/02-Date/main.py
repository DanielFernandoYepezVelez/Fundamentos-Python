""" Importando El Modulo De Fechas, Propio De Python """
import datetime

fechaActual = datetime.date.today()
fechaYhora = datetime.datetime.now()
anio = fechaActual.year
mes = fechaActual.month
dia = fechaActual.day
timeStamp = fechaYhora.timestamp()
fechaPersonalizada = fechaActual.strftime('%d/%m/%Y')
fechaPersonalizada2 = fechaYhora.strftime('%d/%m/%Y, %H:%M:%S')

print('Fecha Actual: ', fechaActual)
print('Fecha Y Hora: ', fechaYhora)
print('Año: ', anio)
print('Mes: ', mes)
print('Dia: ', dia)
print('TimeStamp: ', timeStamp)
print('Fecha Personalizada: ', fechaPersonalizada)
print('Fecha Personalizada2: ', fechaPersonalizada2)