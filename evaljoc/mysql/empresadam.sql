/* Creación y Uso de la Base de Datos */

CREATE DATABASE empresadam;
-- Crea una nueva base de datos con el nombre empresadam
-- Es el primer paso para establecer el entorno de trabajo
-- Consejo: Usar nombres descriptivos y en minúsculas

USE empresadam;
-- Selecciona la base de datos empresadam como la base de datos activa para las siguientes operaciones
-- Necesario para ejecutar comandos DDL (como CREATE TABLE) y DML (como INSERT) sin especificar la base de datos cada vez
-- Consejo: Siempre usar este comando antes de trabajar con tablas


/* Definicion y Estructura de la Tabla "clientes" */

CREATE TABLE clientes(
-- Inicia la definición de la nueva tabla llamada clientes
-- Se usa para definir la estructura inicial de almacenamiento de datos
-- Consejo: Utilizar el formato multilinea para mejor legibilidad

dni VARCHAR(20) NOT NULL;
-- Crea la columna "dni", tipo VARCHAR (cadena de longitud variable) de hasta 20 caracteres y obliga a que siempre tenga un valor (NOT NULL)
-- Se usa para almacenar el DNI de forma única. VARCHAR es ideal para identificadores alfanuméricos
-- Consejo: Usar NOT NULL en campos esenciales para la integridad de los datos
-- Sintaxis: nombre_columna TIPO_DATO(tamaño) RESTRICCIÓN

nombre VARCHAR(50) NOT NULL;
-- Crea la columna nombre, tipo VARCHAR de hasta 50 caracteres, y exige un valor (NOT NULL)
-- Se usa para almacenar el nombre del cliente
-- Sintaxis: nombre_columna VARCHAR(50) NOT NULL

apellidos VARCHAR(100) NOT NULL;
-- Almacena los apellidos del cliente

email VARCHAR(100) NOT NULL;
-- Almacena el email del cliente

CONSTRAINT chk_nombre_min_5 CHECK (CHAR_LENGTH(nombre >= 5))
-- Añade una CONSTRAINT (restricción) que usa CHECK para asegurar que la longitud del campo nombre sea de al menos 5 caracteres
-- Aplicar reglas de negocio para validar la calidad de los datos al insertarlos o actualizarlos
-- Consejo: Usar CHECK para validaciones simples
-- Sintaxis: CONSTRAINT nombre_restricción CHECK (condición) CHAR_LENGTH
-- -- es una función para obtener la longitud de la cadena
);
-- Finaliza la definición de la tabla

ALTER TABLE clientes ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;
-- Modifica la tabla (ALTER TABLE) para añadir una columna (ADD COLUMN) llamada identificador de tipo INT, que se **AUTO_INCREMENT**a y se establece como PRIMARY KEY (clave )
-- Sirve para establecer una clave primaria sintética para identificar unívocamente cada fila, esencial para la integridad de los datos y las relaciones
-- Consejo: Usar una clave primaria auto-incremental es la práctica recomendada para identificar filas
-- Sintaxis ALTER TABLE nombre_tabla ADD COLUMN nombre_columna TIPO_DATO AUTO_INCREMENT PRIMARY KEY ,,FIRST,(opcional)


/* Aplicación Práctica: Inserción y Consulta de Datos" */

INSERT INTO clientes(
 dni, nombre, apellidos, email
) VALUES (
    '54417861E', 'Nicolás', 'García Terrén', 'naitchhh@gmail.com'
);
-- Inserta una nueva fila en la tabla "clientes", especificando los valores para las columnas "dni", "nombre", "apellidos" e "email". El campo "identificador" se auto-genera
-- Se usa para introducir información en la base de datos (operación Create del CRUD)
-- Consejo: Listar las columnas explícitamente es una buena p`ráctica para prevenir errores si la estructura de la tabla cambia
-- Sintaxis: INSERT INTO nombre_tabla (columnas) VALUES (valores). Las cadenas de texto van entre comillas simples

SELECT * FROM clientes;
-- Recupera y muestra todas las columnas (*) de todas las filas (FROM clientes) de la tabla "clientes"
-- Se usa para verificar los datos introducidos (operación Read del CRUD) y recuperar información para el usuario o la aplicación
-- Consejo: Usar SELECT * solo para pruebas; en producción, lista solo las columnas que necesites para optimizar el rendimiento

DESCRIBE clientes;
-- Muestra la estructura (esquema) de la tabla "clientes", incluyendo columnas, tipos de datos, si aceptan nulos, y la clave primaria
-- Sirve para verificar que las restricciones, tipos de datos y la clave primaria se hayan aplicado correctamente
-- Consejo: Útil para depurar y confirmar la estructura
-- Sintaxis: DESCRIBE nombre_tabla o DESC nombre_tabla

