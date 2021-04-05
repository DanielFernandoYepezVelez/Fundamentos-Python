""" Es El Encapsulamiento De Los Métodos,
Que Apesar De Utilizar Dichos Métodos, No Se
Puede Acceder A Ellos Para Modificarlos """

class Restaurant:

    """ MODIFICADORES DE ACCESO """
    # PUBLIC: nombrePropiedad
    # PROTECTED: _nombrePropiedad
    # PRIVATE: __nombrePropiedad

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.__categoria = categoria #PRIVATE
        self._precio = precio # PROTECTED

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoría: {self.__categoria}, Precio: {self._precio}')

# Instanciar La Clase
restaurant = Restaurant('La Esquina De Don Quijote', 'Comida Italiana', 50)

print(restaurant)
restaurant.__categoria = 'Comida Antioqueña' # No Es Posible Modificarlo Por Que Es Private
restaurant._precio = 80
restaurant.mostrar_informacion()