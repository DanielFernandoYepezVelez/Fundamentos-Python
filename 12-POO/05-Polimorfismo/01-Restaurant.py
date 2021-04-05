class Restaurant:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self._categoria = categoria #PROTECTED
        self._precio = precio # PROTECTED

    """ GETTERS AND SETTERS """
    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoría: {self.__categoria}, Precio: {self._precio}')

# --------------------------------------------

""" CLASE QUE HEREDA DE RESTAURANT """
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, alberca):
        super().__init__(nombre, categoria, precio)
        self.alberca = alberca

    """ Método Solo Para El Hotel """
    def get_alberca(self):
        return self.alberca

    """ SOBRE-ESCRIBIENDO EL MÉTODO DEL PADRE RESTAURANT """
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoría: {self._categoria}, Precio: {self._precio}, Alberca: {self.alberca}')

hotel = Hotel('Hotel POO', '5 Estrellas', 200, 'SI')

alberca = hotel.get_alberca()
print(alberca)

hotel.mostrar_informacion();