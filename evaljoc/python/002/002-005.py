# Definición de la clase Carretera con método estático
class Carretera:
    @staticmethod
    def calcular_area(longitud, ancho):
        """
        Calcula el área de la carretera.
        Parámetros:
        - longitud: longitud de la carretera en metros
        - ancho: ancho de la carretera en metros
        Retorna:
        - área en metros cuadrados
        """
        return longitud * ancho

# Ejemplo práctico: calcular el asfalto para una carretera de 500 metros de largo y 12 metros de ancho
longitud_carretera = 500  # en metros
ancho_carretera = 12      # en metros

# Llamada al método estático
area_asfalto = Carretera.calcular_area(longitud_carretera, ancho_carretera)

# Mostrar el resultado
print(f"Área de la carretera: {area_asfalto} metros cuadrados")
print(f"Cantidad de asfalto necesaria: {area_asfalto} metros cuadrados")
