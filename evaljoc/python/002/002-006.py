import math

# Paso 1: Crear objeto cilindro usando un diccionario
cilindro = {
    "radio": 5,   # en metros
    "altura": 10  # en metros
}

# Paso 2: Función para calcular volumen del cilindro
def calcular_volumen(cil):
    return math.pi * cil["radio"]**2 * cil["altura"]

# Paso 3: Función para calcular área superficial del cilindro
def calcular_area_superficial(cil):
    return 2 * math.pi * cil["radio"] * (cil["altura"] + cil["radio"])

# Paso 4: Calcular volumen y área superficial
volumen = calcular_volumen(cilindro)
area_superficial = calcular_area_superficial(cilindro)

# Paso 5: Imprimir resultados
print(f"Volumen del cilindro: {volumen:.2f} m³")
print(f"Área superficial del cilindro: {area_superficial:.2f} m²")
