# Importamos Flask para poder crear la aplicación web
from flask import Flask

# Importamos mysql.connector para conectar Python con la base de datos MySQL
import mysql.connector

# Creamos la aplicación Flask, que se encargará de recibir solicitudes y devolver respuestas
app = Flask(__name__)

# Definimos la ruta principal '/' de nuestra web
# Esto significa que cuando abramos localhost:5000/ se ejecutará esta función
@app.route('/')
def portafolio():
    # --- Conexión a MySQL ---
    # Creamos la conexión con la base de datos que ya hemos creado
    conexion = mysql.connector.connect(
        host="localhost",           # Servidor local donde está la base de datos
        user="portafolioexamen2",  # Usuario creado para la base de datos
        password="Aladin12345&",   # Contraseña del usuario
        database="portafolioexamen2"  # Nombre de la base de datos
    )

    # Creamos un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()
    
    # Ejecutamos la consulta SQL para obtener todas las piezas y su categoría
    cursor.execute("""
        SELECT p.titulo, p.descripcion, p.fecha, c.nombre AS categoria
        FROM piezasportafolio p
        JOIN categoriasportafolio c ON p.id_categoria = c.id
    """)
    
    # Guardamos los resultados en la variable 'piezas', que será una lista de tuplas
    piezas = cursor.fetchall()
    
    # Cerramos el cursor y la conexión para liberar recursos
    cursor.close()
    conexion.close()

    # --- Creamos el HTML dinámicamente ---
    # Inicializamos la variable 'html' con la estructura básica de la página
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8"> <!-- Definimos la codificación de caracteres -->
        <title>Portafolio Intermodular</title> <!-- Título que aparece en la pestaña del navegador -->
        <style>
            /* Estilos CSS internos */
            body {font-family: Arial,sans-serif; background:#f5f5f5; margin:0;} /* Fuente y fondo general */
            header {background: indigo; color:white; text-align:center; padding:20px;} /* Cabecera */
            section {background:white; width:80%; margin:20px auto; padding:15px; border-radius:8px;} /* Secciones centradas */
            #portafolio {display:grid; grid-template-columns: repeat(3,1fr); gap:20px;} /* Grid para las piezas */
            #portafolio article {background:#fff; padding:10px; border-radius:6px; box-shadow:0 2px 5px rgba(0,0,0,0.1);} /* Estilo de cada pieza */
            #portafolio img {width:100%; border-radius:6px;} /* Imagen adaptada al tamaño del artículo */
        </style>
    </head>
    <body>
    <header>
        <h1>Portafolio Intermodular</h1> <!-- Título principal -->
    </header>
    <section id="portafolio"> <!-- Sección donde se mostrarán todas las piezas -->
    """

    # --- Añadimos los artículos del portafolio de forma dinámica ---
    for titulo, descripcion, fecha, categoria in piezas:
        # Recorremos cada tupla de la lista 'piezas' y añadimos un artículo por cada pieza
        html += f"""
        <article>
            <h4>{titulo}</h4> <!-- Mostramos el título de la pieza -->
            <p>Descripción: {descripcion}</p> <!-- Mostramos la descripción -->
            <p>Categoría: {categoria}</p> <!-- Mostramos la categoría -->
            <p>Fecha: {fecha}</p> <!-- Mostramos la fecha -->
            <img src="/static/foto_default.jpg" alt="{titulo}"> <!-- Imagen por defecto -->
        </article>
        """

    # --- Cerramos el HTML ---
    html += """
    </section>
    <footer style="text-align:center; padding:15px; background:indigo; color:white;">
        Proyecto Intermodular - 1º DAW <!-- Pie de página -->
    </footer>
    </body>
    </html>
    """

    # Devolvemos el HTML completo como respuesta al navegador
    return html

# Arrancamos la aplicación Flask
# debug=True sirve para que se muestren los errores en pantalla y se recargue automáticamente al cambiar el código
if __name__ == '__main__':
    app.run(debug=True)
