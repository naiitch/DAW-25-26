# Definición de la clase Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Creación de un objeto de la clase Producto
producto1 = Producto("Laptop", 1200)

# Mostrar los valores de las propiedades del producto
print("Nombre del producto:", producto1.nombre)
print("Precio del producto:", producto1.precio, "€")
