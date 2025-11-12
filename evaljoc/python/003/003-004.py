# Programa para calcular el precio final de un coche incluyendo impuestos
while True:
    try:
        # Solicitar datos al usuario
        precio_base = float(input("Introduce el precio base del coche en euros: "))
        impuesto = float(input("Introduce la tasa de impuesto (%) del coche: "))

        # Validación de valores positivos
        if precio_base < 0 or impuesto < 0:
            raise ValueError("Los valores deben ser positivos")

        # Cálculo del precio final
        precio_final = precio_base * (1 + impuesto / 100)

        # Mostrar resultado
        print(f"El precio final del coche, incluyendo impuestos, es: {precio_final:.2f} euros")
        break  # Salir del bucle si todo está correcto

    except:
        print("Error, prueba de nuevo.")
