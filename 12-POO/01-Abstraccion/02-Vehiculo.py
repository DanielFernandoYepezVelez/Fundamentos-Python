class Vehiculo:
    """ Atributos - Propiedades - Estado """
    color = 'Rojo'
    marca = 'Ferrari'
    modelo = 'Aventador'
    velocidad = 300
    caballaje = 500
    puertas = 2

    """ Métodos - Acciones - Lo Que Puede Hacer El Vehiculo, Sin Perder El Contexto """
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

""" Instanciando La Clase O Creando Un Objeto De La Misma """
vehiculo = Vehiculo()

print(vehiculo)
print(vehiculo.marca)
print(vehiculo.color)

print('Velocidad Inicial: ', vehiculo.velocidad)
vehiculo.acelerar()
vehiculo.acelerar()
vehiculo.acelerar()
vehiculo.acelerar()
print('Velocidad Despues De Acelerar: ', vehiculo.velocidad)
vehiculo.frenar()
vehiculo.frenar()
print('Velocidad Despues De Frenar: ', vehiculo.velocidad)