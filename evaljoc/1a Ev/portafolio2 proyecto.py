# Importamos Flask y funciones necesarias
from flask import Flask, render_template
import mysql.connector

# Creamos la app Flask
app = Flask(__name__)

# Función para conectar a la base de datos y obtener las piezas con categorías
def obtener_piezas():
    # Conexión a MySQL
    conexion = mysql.connector.connect(
        host="localhost",
        user="portafolioexamen2",
        password="Aladin12345&",
        database="portafolioexamen2"
    )
    cursor = conexion.cursor(dictionary=True)  # Diccionario para acceder con nombres de columna
    # Consulta SQL con LEFT JOIN para unir piezas con categorías
    cursor.execute("""
        SELECT p.titulo, p.descripcion, p.fecha, c.nombre AS categoria
        FROM piezasportafolio p
        LEFT JOIN categoriasportafolio c ON p.id_categoria = c.id
    """)
    piezas = cursor.fetchall()  # Obtenemos todos los resultados
    cursor.close()
    conexion.close()
    return piezas

# Ruta principal de la web
@app.route("/")
def index():
    piezas = obtener_piezas()  # Obtenemos los datos
    return render_template("index.html", piezas=piezas)  # Pasamos los datos al HTML

# Ejecuta la app en modo debug
if __name__ == "__main__":
    app.run(debug=True)
