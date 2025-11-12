from datetime import datetime
import random

# Paso 1: Fecha actual
coche_actual = datetime.now()

# Paso 2: Método para obtener el año actual
def get_year(fecha):
    return fecha.year

# Paso 3: Método para obtener el mes en formato completo
def get_mes_completo(fecha):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    return meses[fecha.month - 1]  # month devuelve 1-12, lista usa índice 0-11

# Paso 4: Número aleatorio entre 0 y 1
numero_aleatorio = random.random()

# Paso 5: Redondear el número aleatorio a dos decimales
numero_redondeado = round(numero_aleatorio, 2)

# Paso 6: Imprimir resultados
print("Año actual:", get_year(coche_actual))
print("Mes actual:", get_mes_completo(coche_actual))
print("Número aleatorio redondeado:", numero_redondeado)
