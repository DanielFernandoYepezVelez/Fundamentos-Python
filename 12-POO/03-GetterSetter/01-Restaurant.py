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
        
# Instanciar La Clase
restaurant = Restaurant('La Esquina De Don Quijote', 'Comida Italiana', 50)

print(restaurant)
print(restaurant.get_categoria())

restaurant.set_categoria('Comida Antioqueña')
print(restaurant.get_categoria())

restaurant._precio = 80
restaurant.mostrar_informacion()