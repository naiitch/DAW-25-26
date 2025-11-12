from datetime import datetime

# Paso 1: Crear objeto fecha actual
fecha_actual = datetime.now()

# Lista de días de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Paso 2: Función para obtener el año completo
def obtener_anio_completo():
    return fecha_actual.year

# Paso 3: Función para obtener el día de la semana
def obtener_dia_semana():
    numero_dia = fecha_actual.weekday()  # 0 = lunes, 6 = domingo
    return dias_semana[numero_dia]

# Paso 4: Llamar a las funciones y almacenar resultados
anio_completo = obtener_anio_completo()
dia_semana = obtener_dia_semana()

# Paso 5: Imprimir resultados
print("Año completo:", anio_completo)
print("Día de la semana:", dia_semana)
