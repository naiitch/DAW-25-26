'''
    Programa de Registro y Gestión de Clientes
    v0.1 - Nicolás García Terrén
    Esta aplicación registra datos asociados a un cliente concreto y
    puede mostrar un listado de éstos
'''


class Cliente():
    def __init__(self):  # No utilizo ningún parámetro adicional en el constructor __init__
        self.email = None
        self.nombre = None
        self.direccion = None


cliente1 = Cliente()
cliente1.nombre = input("Introduce el nombre del cliente: ")
cliente1.email = input("Introduce el email del cliente: ")
cliente1.direccion = input("Introduce la dirección del cliente: ")

clientes = [] # Creo una lista vacía

clientes.append(cliente1) # Guardo el cliente inicial (cliente1) a la lista
print("Cliente añadido satisfactoriamente")

while True: # Esto desata un bucle infinito pero controlado

    # Muestro el menú de interacción que utilizará el usuario
    print("\nMenú de interacción: ")
    print("1.-Insertar un cliente")
    print("2.-Listar clientes")
    print("3.-Actualizar clientes")
    print("4.-Eliminar clientes")
    print("5.-Salir del menú")

    # Le permito escoger una opción
    opcion = input("Escoge una opción: ")
    opcion = int(opcion)  # Convierto la opción númerica de string a entero
    
    if opcion == 1:
        print("\nVamos a insertar un cliente")
        nuevocliente = Cliente()
        nuevocliente.nombre = input("Introduce el nombre del cliente: ")
        nuevocliente.email = input("Introduce el email del cliente: ")
        nuevocliente.direccion = input("Introduce la direccion del cliente: ")
        # A la lista de clientes añadimos nuestro cliente
        clientes.append(nuevocliente)
        print("Cliente añadido satisfactoriamente") # Breve mensaje de confirmación sobre la correcta entrada de datos

    elif opcion == 2:
        print("\nVamos a ver los clientes")
        if len(clientes) == 0: # Compruebo la longitud de la lista, en caso de ser nula (no hay elementos), no habrán clientes listados
            print("No hay clientes listados")
        else:
            # Bucle para mostrar los clientes
            contador = 1
            for cliente in clientes: # cliente es una variable temporal que Python crea de manera implícita al inicio del bucle, producto de ser un lenguaje de alto nivel
                print(f"Cliente: {contador}")
                print(f"Nombre: {cliente.nombre}")
                print(f"Email: {cliente.email}")
                print(f"Dirección: {cliente.direccion}")
                contador += 1 # El contador se actualiza con cada ciclo del bucle for
    elif opcion == 3:
        print("Vamos a actualizar los clientes")
    
    elif opcion == 4:
        print("Vamos a eliminar un cliente")
    
    elif opcion == 5:
        break
    else:
        print("Selecciona una opción de entre las listadas")