import random
from datetime import datetime

# Paso 1: Fecha de construcción
fecha_construccion = datetime.now()

# Paso 2: Longitud del puente (entre 100 y 1000 metros)
longitud_metros = random.randint(100, 1000)

# Paso 3: Número del puente (entre 1 y 50)
numero_puente = random.randint(1, 50)

# Paso 4: Tipo de material
tipos_materiales = ["concreto", "acero", "fibrocemento"]
tipo_material = random.choice(tipos_materiales)

# Paso 5: Costo del puente (entre 10,000,000 y 20,000,000 euros)
costo = random.randint(10_000_000, 20_000_000)

# Creación del objeto Puente
puente = {
    "fecha_construccion": fecha_construccion,
    "longitud_metros": longitud_metros,
    "numero_puente": numero_puente,
    "tipo_material": tipo_material,
    "costo": costo
}

# Impresión de la información del puente
print(f"Puente número {puente['numero_puente']}")
print("Fecha de construcción:", puente['fecha_construccion'].strftime("%d/%m/%Y"))
print(f"Longitud: {puente['longitud_metros']} metros")
print(f"Tipo de material: {puente['tipo_material']}")
print(f"Costo: {puente['costo']} euros")
