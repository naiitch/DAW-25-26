# Definición de la clase Edificio
class Edificio:
    def __init__(self, altura, numero_pisos, material):
        self.altura = altura
        self.numero_pisos = numero_pisos
        self.material = material

    def calcular_costo(self):
        """
        Calcula el costo de construcción del edificio.
        Suposición: precio por metro cuadrado según material.
        """
        # Precio unitario por metro cuadrado según material
        precios_material = {
            "acero": 1200,
            "hormigon": 1000,
            "madera": 800
        }
        precio_unitario = precios_material.get(self.material.lower(), 1000)
        
        # Supongamos que cada piso tiene 100 m² por simplicidad
        area_total = self.numero_pisos * 100  # área total en m²
        # Costo total
        return area_total * precio_unitario

# Crear una instancia de Edificio
mi_edificio = Edificio(altura=50, numero_pisos=10, material="acero")

# Calcular costo
costo_total = mi_edificio.calcular_costo()

# Mostrar resultado
print(f"Costo de construcción del edificio: {costo_total} euros")
