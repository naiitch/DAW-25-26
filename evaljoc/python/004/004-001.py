class Gato():
    def __init__(self):
        self.color = ""
        self.nombre = ""
# Crear una instancia de gato
gato1 = Gato()

#Asignar atributos al gato1
gato1.nombre = "Garfield"
gato1.color = "naranja"

# Imprimir gato1
print(gato1)

#Crear una segunda instancia de gato
gato2 = Gato()

# Asignar atributos a gato2
gato2.nombre = "Gustavo"
gato2.color = "naranja"

# Imprimir gato2
print(gato2)

# Modificar el color de gato1

gato1.color = "verde"

# Imprimir gato1 después del cambio
print(gato1)