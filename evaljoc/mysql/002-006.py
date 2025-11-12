import sqlite3
# SQLite es un sitema de base de datos ligero y embebido (no necesita instalación como My SQL)
#Guarda los datos en un solo archivo .db
#Importar sqlite3 basta para crear bases de datos SQL scompletas sin depender de un servidor
# De este modo no necesito instalar nada con pip

# Cada vez que trabaje con una base de datos SQLite debo seguir estos pasos básicos:
'''
# 1. Importar la librería
import sqlite3

# 2. Conectarte (si no existe, se crea)
conexion = sqlite3.connect("empresa.db")

# 3. Crear un cursor (permite ejecutar comandos SQL)
cursor = conexion.cursor()

# 4. Ejecutar tus comandos SQL
cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nombre TEXT)")

# 5. Confirmar los cambios (como un 'guardar')
conexion.commit()

# 6. Cerrar la conexión
conexion.close()
'''
# Estos 6 pasos son la base para hacer cualquier CRUD con SQLite

# En SQLite se pone AUTOINCREMENT todo junto, no con guión bajo como en MySQL

# Conexión y creación de la tabla

def crear_tabla():
    conexion = sqlite3.connect("empresa.db")
    cursor = conexion.cursor()  # Creamos un cursor, que es el intermediario para ejecutar SQL

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        telefono TEXT
    )
    """)

    conexion.commit()  # Guardamos los cambios
    conexion.close()   # Cerramos la conexión
    print("La tabla clientes ha sido creada.\n")

# Crear un cliente

def crear_cliente(nombre,email,telefono):
    try:
        conexion = sqlite3.connect("empresa.db")
        cursor = conexion.cursor()

        # Insertamos datos usando "?" ya que evita errores o inyección SQL
        cursor.execute("INSERT INTO clientes (nombre,email,telefono) VALUES (?,?,?)",
                       (nombre,email,telefono))
        conexion.commit()
        print(f"Cliente '{nombre}' creado correctamente. \n")

    except:
        # Esto ocurre si el email ya existe (porque pusimos UNIQUE)
        print( "Error: El email ya existe en la base de datos. \n")
    
    finally:
        # Se cierra la conexión, ocurra o no un error
        conexion.close()

# Listar clientes
def listar_clientes():
    conexion = sqlite3.connect("empresa.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()  # Recupera todos los registros

    if clientes:
        print(" Lista de clientes:")
        for cliente in clientes:
            # cliente es una tupla, no una lista. Es una colección ordenada e inmutable de elementos (id, nombre, email, telefono)
            print(f"ID: {cliente[0]} | Nombre: {cliente[1]} | Email: {cliente[2]} | Teléfono: {cliente[3]}")
    else:
        print(" No hay clientes registrados.")

    print()  # Línea en blanco para separar
    conexion.close()

# Actualizar clientes
def actualizar_cliente(id_cliente, nuevo_nombre, nuevo_email, nuevo_telefono):
    conexion = sqlite3.connect("empresa.db")
    cursor = conexion.cursor()

    # Actualizamos un registro según su ID
    cursor.execute("""
        UPDATE clientes
        SET nombre = ?, email = ?, telefono = ?
        WHERE id = ?
    """, (nuevo_nombre, nuevo_email, nuevo_telefono, id_cliente))

    conexion.commit()

    if cursor.rowcount == 0:
        print(f"No se encontró un cliente con ID {id_cliente}.\n")
    else:
        print(f"Cliente con ID {id_cliente} actualizado correctamente.\n")

    conexion.close()

# Eliminar clientes

def eliminar_cliente(id_cliente):
    conexion = sqlite3.connect("empresa.db")
    cursor = conexion.cursor()

    # Eliminamos el registro con el ID indicado
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
    conexion.commit()

    if cursor.rowcount == 0:
        print(f"No se encontró un cliente con ID {id_cliente}.\n")
    else:
        print(f"Cliente con ID {id_cliente} eliminado correctamente.\n")

    conexion.close()

# Programa principal de prueba
if __name__ == "__main__":
    # Creamos la tabla
    crear_tabla()

    # Creamos clientes
    crear_cliente("Nicolás García", "nico@gmail.com", "611133052")
    crear_cliente("Nacho Vidal", "nacho@hotmail.com", "699887766")
    crear_cliente("Nicolás García", "nico@gmail.com", "611133052")  # Duplicado (error controlado)

    # Listamos todos los clientes
    listar_clientes()

    # Actualizamos un cliente existente (ID 1)
    actualizar_cliente(1, "Nicolás G. Terrén", "naitch@disroot.org", "611133051")

    # Listar después de actualizar
    listar_clientes()

    # Eliminar cliente
    eliminar_cliente(2)

    # Intentar eliminar uno que no existe
    eliminar_cliente(10)

    # Listar final
    listar_clientes()

'''
La tabla clientes ha sido creada.

Cliente 'Nicolás García' creado correctamente.

Cliente 'Nacho Vidal' creado correctamente.

Error: El email ya existe en la base de datos.

 Lista de clientes:
ID: 1 | Nombre: Nicolás García | Email: nico@gmail.com | Teléfono: 611133052        
ID: 2 | Nombre: Nacho Vidal | Email: nacho@hotmail.com | Teléfono: 699887766        

Cliente con ID 1 actualizado correctamente.

 Lista de clientes:
ID: 1 | Nombre: Nicolás G. Terrén | Email: naitch@disroot.org | Teléfono: 611133051 
ID: 2 | Nombre: Nacho Vidal | Email: nacho@hotmail.com | Teléfono: 699887766        

Cliente con ID 2 eliminado correctamente.

No se encontró un cliente con ID 10.

 Lista de clientes:
ID: 1 | Nombre: Nicolás G. Terrén | Email: naitch@disroot.org | Teléfono: 611133051
'''