# Ejemplo práctico combinando coches y estructuras

# Solicitar datos al usuario
edad_conductor = int(input("Introduce la edad del conductor: "))
altura_estructura = float(input("Introduce la altura de la estructura en metros: "))

# Validación de datos mediante aserciones
assert edad_conductor >= 18, "Error: El conductor debe ser mayor de 18 años"
assert altura_estructura >= 5, "Error: La altura de la estructura es demasiado baja"

# Mostrar resultados si todo está correcto
print("Todos los datos son correctos. Puedes continuar con el proyecto.")

# Ejemplos adicionales de aserciones
# Edad del conductor
edad_conductor = 20
assert edad_conductor >= 18, "Error: El conductor debe ser mayor de 18 años"

# Altura de la estructura
altura_estructura_calculada = 15.5  # metros
altura_minima_requerida = 10
assert altura_estructura_calculada >= altura_minima_requerida, "Error: La altura de la estructura es insuficiente"

print("Ejemplos adicionales: todos los cálculos son correctos")
