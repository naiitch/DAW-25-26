def calcular_velocidad(kilometros, horas):
    if horas != 0:
        velocidad = kilometros/horas
        return velocidad
    else:
        return "Error: No se puede dividir por cero"

for horas in range(1,6):
    for kilometros in range(10, 50, 10):
        print(f"Horas: {horas}, Kilómetros: {kilometros}, velocidad: {calcular_velocidad(kilometros, horas)} km/h")