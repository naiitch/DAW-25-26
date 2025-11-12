
#Declaración de variables
anio_inicio = 0 #Año inicial del rango
anio_fin = 0 #Año final del rango
nombre_cronista = "" #Nombre del cronista para el encabezado

#Entrada de datos
nombre_cronista = input("Querido cronista, introduzca su nombre: ")
anio_inicio = int(input("Introduce el año de inicio del rango: "))
anio_fin = int(input("Introduce el año donde acaba el rango: "))

#Estructuras de selección

# Defino una función
# Las funciones agrupan un bloque de código para una tarea específica,
# haciendo el código más organizado, fácil de entender y reutilizable
# Esta función en concreto toma un argumento ('anio') y devuelve ('return') un string

def clasificar_etapa_historica(anio):
    if 476 <= anio < 1500:
        return "Edad Civil - Caída del imperio romano e inicio del feudalismo. "
    
    elif 1500 <= anio < 1800:
        return "Edad Moderna - Descubrimiento de América y movimientos renacentistas e ilustrados. "
    
    else:
        return " Edad Contemporánea - Revolución francesa, Guerras Munidales, primer alunizaje humano. "
    
def cronista_linea_temporal(anio_inicio, anio_fin, nombre_cronista=None):
    if nombre_cronista:
        print(f"Encabezado: {nombre_cronista}")
    
    for anio in range(anio_inicio, anio_fin + 1):
        etapa = clasificar_etapa_historica(anio)
        print(f"Año {anio}: {etapa}")
        

