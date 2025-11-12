# Definición de la clase Cliente
class Cliente:
    def __init__(self):
        self.__nombrecompleto = ""
        self.__email = ""

    # Setter y Getter para nombrecompleto
    def setNombreCompleto(self, nuevonombre):
        self.__nombrecompleto = nuevonombre

    def getNombreCompleto(self):
        return self.__nombrecompleto

    # Setter y Getter para email
    def setEmail(self, nuevoemail):
        self.__email = nuevoemail

    def getEmail(self):
        return self.__email

# Creación de una instancia de Cliente
cliente1 = Cliente()

# Asignar valores usando setters
cliente1.setNombreCompleto("Nicolás García")
cliente1.setEmail("naitch@disroot.org")

# Mostrar los valores usando getters
print("Nombre del cliente:", cliente1.getNombreCompleto())
print("Correo electrónico:", cliente1.getEmail())
