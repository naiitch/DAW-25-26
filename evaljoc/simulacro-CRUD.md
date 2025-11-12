Perfecto, vamos a desglosar tu problema paso a paso y te voy a dar un ejemplo completo para que puedas implementarlo tal como un examen lo pediría. Lo dividiremos en Base de Datos y Aplicación Python consola CRUD.

Paso 1: Base de Datos MySQL
1.1 Crear las tablas
CREATE DATABASE IF NOT EXISTS portafolio;
USE portafolio;

-- Tabla Categoría
CREATE TABLE Categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    descripcion TEXT
);

-- Tabla Pieza
CREATE TABLE Pieza (
    id_pieza INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    descripcion TEXT,
    imagen VARCHAR(255),
    url VARCHAR(255),
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
);

1.2 Insertar algunos datos de prueba
-- Categorías
INSERT INTO Categoria (titulo, descripcion) VALUES
('Fotografía', 'Obras de fotografía artística'),
('Pintura', 'Obras de pintura tradicional');

-- Piezas
INSERT INTO Pieza (titulo, descripcion, imagen, url, id_categoria) VALUES
('Atardecer', 'Fotografía de un atardecer en la playa', 'atardecer.jpg', 'http://miportafolio.com/atardecer', 1),
('Retrato', 'Pintura al óleo de un retrato', 'retrato.jpg', 'http://miportafolio.com/retrato', 2);

1.3 Crear un JOIN y una VIEW
-- JOIN entre Pieza y Categoria
SELECT p.id_pieza, p.titulo AS pieza, p.descripcion AS descripcion_pieza,
       p.imagen, p.url, c.titulo AS categoria, c.descripcion AS descripcion_categoria
FROM Pieza p
JOIN Categoria c ON p.id_categoria = c.id_categoria;

-- Crear una vista para usarla después
CREATE VIEW vista_piezas AS
SELECT p.id_pieza, p.titulo AS pieza, p.descripcion AS descripcion_pieza,
       p.imagen, p.url, c.titulo AS categoria, c.descripcion AS descripcion_categoria
FROM Pieza p
JOIN Categoria c ON p.id_categoria = c.id_categoria;

Paso 2: Aplicación Python - Consola CRUD

Vamos a usar mysql-connector-python. Primero instálalo si no lo tienes:

pip install mysql-connector-python

2.1 Código completo de ejemplo
import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Cambia por tu contraseña
    database="portafolio"
)

cursor = conexion.cursor()

# Mensaje de bienvenida
print("=== Bienvenido al sistema de administración de Portafolio ===")

while True:
    print("\nOpciones:")
    print("1. Ver todas las piezas")
    print("2. Agregar una nueva pieza")
    print("3. Actualizar una pieza")
    print("4. Eliminar una pieza")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        cursor.execute("SELECT * FROM vista_piezas")
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)

    elif opcion == "2":
        titulo = input("Título de la pieza: ")
        descripcion = input("Descripción: ")
        imagen = input("Nombre de la imagen: ")
        url = input("URL de la pieza: ")
        id_categoria = input("ID de la categoría: ")
        cursor.execute(
            "INSERT INTO Pieza (titulo, descripcion, imagen, url, id_categoria) VALUES (%s, %s, %s, %s, %s)",
            (titulo, descripcion, imagen, url, id_categoria)
        )
        conexion.commit()
        print("Pieza agregada correctamente.")

    elif opcion == "3":
        id_pieza = input("ID de la pieza a actualizar: ")
        nuevo_titulo = input("Nuevo título: ")
        nuevo_descripcion = input("Nueva descripción: ")
        cursor.execute(
            "UPDATE Pieza SET titulo=%s, descripcion=%s WHERE id_pieza=%s",
            (nuevo_titulo, nuevo_descripcion, id_pieza)
        )
        conexion.commit()
        print("Pieza actualizada correctamente.")

    elif opcion == "4":
        id_pieza = input("ID de la pieza a eliminar: ")
        cursor.execute("DELETE FROM Pieza WHERE id_pieza=%s", (id_pieza,))
        conexion.commit()
        print("Pieza eliminada correctamente.")

    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")

# Cerrar conexión
cursor.close()
conexion.close()

✅ Qué hace el código

Se conecta a MySQL.

Muestra un menú infinito con opciones CRUD.

Usa if-elif para decidir qué operación ejecutar.

Ejecuta SELECT, INSERT, UPDATE y DELETE sobre la base de datos.

Usa la vista para mostrar un JOIN entre Pieza y Categoria.