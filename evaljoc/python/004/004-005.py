# Definición de la clase Coche
class Coche:
    def __init__(self, marca, modelo, potencia):
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia

    # Método para mostrar la información del coche
    def mostrar_info(self):
        return f"El coche es marca {self.marca}, modelo {self.modelo} y tiene {self.potencia} CV."

# Creación de un objeto de la clase Coche
coche1 = Coche("Volkswagen", "Golf", 105)

# Llamada al método para mostrar la información
print(coche1.mostrar_info())
