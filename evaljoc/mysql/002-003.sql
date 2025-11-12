-- Muestro las bases de datos y selecciono empresadam
SHOW DATABASES:
+--------------------+
| Database           |
+--------------------+
| empresadam         |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+

USE empresadam;
Database changed


-- 1. Mostrar las tablas existentes para verificar si ya hay alguna
SHOW TABLES;
Empty set (0.00 sec)


-- 2. Crear tabla 'clientes' donde se almacenará la información de cada cliente
CREATE TABLE clientes (
    dni VARCHAR(9) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    telefono VARCHAR(6)
);
Query OK, 0 rows affected (0.02 sec)

-- 3. Inertamos un cliente en la tabla 'clientes'
INSERT INTO clientes(
    dni, nombre, apellidos, email, telefono
) VALUES (
    '54417861E', 'Nicolás', 'García Terrén', 'naitch@disroot.org', '611133051'
);
Query OK, 1 row affected (0.00 sec)

-- 4. Consulto todos los clientes
SELECT * FROM clientes;
+-----------+---------+------------------+-------------------+------------+
| dni       | nombre  | apellidos        | email             | telefono   |
+-----------+---------+------------------+-------------------+------------+
| 54417861E | Nicolás | García Terrén    | naitch@disroot.org| 611133051  |
+-----------+---------+------------------+-------------------+------------+
1 row in set (0.00 sec)


