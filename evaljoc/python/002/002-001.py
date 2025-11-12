# Definimos un coche como un objeto predeterminado usando un diccionario
coche = {
    "color": "rojo",
    "marca": "Ferrari",
    "modelo": "F8"
}

# Función para simular que el coche arranca
def arrancar(coche):
    print(f"El coche {coche['marca']} {coche['modelo']} ha arrancado.")

# Función para simular que el coche se detiene
def detener(coche):
    print(f"El coche {coche['marca']} {coche['modelo']} se ha detenido.")

# Acceso a los atributos del coche
print(f"Color del coche: {coche['color']}")
print(f"Marca del coche: {coche['marca']}")
print(f"Modelo del coche: {coche['modelo']}")

# Invocación de los métodos
arrancar(coche)
detener(coche)
