# Variables iniciales
operando1 = 4
operando2 = 3

# Función suma que recibe dos parámetros y devuelve el resultado
def suma(a, b):
    return a + b

# Llamada a la función pasando los operandos
resultado = suma(operando1, operando2)

# Mostrar el resultado
print("La suma de", operando1, "+", operando2, "es:", resultado)

# Función para operaciones matemáticas generales
def operacionMatematica(tipo, a, b):
    if tipo == "suma":
        return a + b
    elif tipo == "resta":
        return a - b
    elif tipo == "multiplicacion":
        return a * b
    elif tipo == "division":
        if b != 0:
            return a / b
        else:
            return "Error: División por cero"
    else:
        return "Error: Operación no reconocida"

# Ejemplos de uso
print("Resta:", operacionMatematica("resta", operando1, operando2))
print("Multiplicación:", operacionMatematica("multiplicacion", operando1, operando2))
print("División:", operacionMatematica("division", operando1, operando2))
