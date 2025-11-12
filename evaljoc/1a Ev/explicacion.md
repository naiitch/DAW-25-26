se inicializa la aplicación con app = Flask(__name__)
Se define la ruta principal / con @app.route('/')
app.run(debug=True) permite ejecutar el servidor local y detectar errores en tiempo real
a integración con MySQL hace que el contenido sea siempre actualizado
Flask permite crear páginas dinámicas sin depender de plantillas complejas
Con un bucle for se recorre cada registro de la base de datos y se agregan artículos al HTML dinámicamente