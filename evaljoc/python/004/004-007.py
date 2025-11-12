# Definición de la clase madre
class Animal:
    def __init__(self, edad, nombre, raza):
        self.edad = edad    # Atributo edad
        self.nombre = nombre  # Atributo nombre
        self.raza = raza    # Atributo raza

# Clases hijas que heredan de Animal
class Gato(Animal):
    def __init__(self, edad, nombre, raza):
        super().__init__(edad, nombre, raza)  # Inicializa atributos heredados

class Perro(Animal):
    def __init__(self, edad, nombre, raza):
        super().__init__(edad, nombre, raza)  # Inicializa atributos heredados

# Creación de objetos
gato1 = Gato(3, "Max", "Javanés")       # Objeto de tipo Gato
perro1 = Perro(5, "Petruso", "Doberman")    # Objeto de tipo Perro

# Acceso a atributos heredados
print(f"El gato {gato1.nombre} tiene {gato1.edad} años y es de raza {gato1.raza}.")
print(f"El perro {perro1.nombre} tiene {perro1.edad} años y es de raza {perro1.raza}.")
