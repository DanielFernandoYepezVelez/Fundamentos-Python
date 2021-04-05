class Restaurant:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.__categoria = categoria #PRIVATE
        self._precio = precio # PROTECTED

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoría: {self.__categoria}, Precio: {self._precio}')

    """ GETTERS AND SETTERS """
    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, categoria):
        self.__categoria = categoria

""" CLASE QUE HEREDA DE RESTAURANT """
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)

hotel = Hotel('Hotel POO', '5 Estrellas', 200)
hotel.mostrar_informacion();