-- No se utilizan librerías externas

-- 1. Conexión a la Base de Datos
sudo mysql -u root -p

-- 2. Selección de la Base de Datos
USE empresadam;
Database changed

-- 3. Visualización de Tablas
SHOW TABLES;
+------------------+
| Tables_in_empresadam |
+------------------+
| clientes         |
+------------------+
1 row in set (0.00 sec)

-- 4. Consulta de Datos
SELECT * FROM clientes;
DESCRIBE clientes;
+-----------+---------+------------------+--------------------+------------+
| dni       | nombre  | apellidos        | email              | telefono   |
+-----------+---------+------------------+--------------------+------------+
| 54417861E | Nicolás | García Terrén    | naitch@disroot.org | 611133051  |
+-----------+---------+------------------+--------------------+------------+
1 row in set (0.00 sec)

-- 5. Descripción de la Tabla
DESCRIBE clientes;
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| dni       | varchar(9)   | NO   |     | NULL    |       |
| nombre    | varchar(100) | NO   |     | NULL    |       |
| apellidos | varchar(255) | NO   |     | NULL    |       |
| email     | varchar(255) | NO   |     | NULL    |       |
| telefono  | varchar(6)   | YES  |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
5 rows in set (0.00 sec)


-- 6. Creación de Clave Primaria
ALTER TABLE clientes ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;
Query OK, 1 row affected (0.02 sec)
Records: 1  Duplicates: 0  Warnings: 0

-- Este comando agrega una nueva columna identificador con valores enteros que incrementan
-- automáticamente y se establece como clave primaria

-- 7. Verificación de Cambios
DESCRIBE clientes;
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| identificador | int          | NO   | PRI | NULL    | auto_increment |
| dni           | varchar(9)   | NO   |     | NULL    |                |
| nombre        | varchar(100) | NO   |     | NULL    |                |
| apellidos     | varchar(255) | NO   |     | NULL    |                |
| email         | varchar(255) | NO   |     | NULL    |                |
| telefono      | varchar(6)   | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
6 rows in set (0.00 sec)
