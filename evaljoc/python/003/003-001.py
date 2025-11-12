''' 
    Clasificación de Plantas según su Altura 

    v0.1 Nicolas Garcia Terren 

    Este programa recopila la altura de una planta en centímetros y,
    en base a ello, la categoriza como pequeña, mediana o grande.
''' 

# Solicito al usuario que introduzca la altura de la planta y ésta se almacena en una variable
altura_planta = float(input("¿Cual es la altura de la planta? Proporcionala en centímetros, por favor: "))

# Utilizo estructuras se selección / condicionales para clasificar la planta según su altura300
if altura_planta < 50:
    print("La planta se clasifica como pequeña")
elif altura_planta >= 50 and altura_planta <= 100:
    print("La planta se clasifica como mediana")
elif altura_planta > 100:
    print("La planta se clasifica como grande")
