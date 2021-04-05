class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}')

# Instanciar La Clase
restaurant = Restaurant('La Esquina De Don Quijote', 'Comida Italiana', 50)

print(restaurant)
restaurant.mostrar_informacion()