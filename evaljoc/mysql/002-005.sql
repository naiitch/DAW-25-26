sudo mysql -u root -p

USE empresadam;
Database changed


-- 1. Crear la Tabla de Productos
CREATE TABLE productos (
    identificador INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(7,2) NOT NULL,
    stock INT NOT NULL,
-- 2. Crear Restricciones

    CONSTRAINT chk_nombre_min_5 CHECK (CHAR_LENGTH(nombre) >= 5),
    --  El nombre del producto debe tener al menos 5 caracteres

    CONSTRAINT chk_precio_no_negativo CHECK (precio >= 0),
    -- El precio del producto no puede ser negativo

    CONSTRAINT chk_precio_max_5000 CHECK (precio <= 5000),
    -- El precio del producto no puede superar los 5000 euros

    CONSTRAINT chk_stock_no_negativo CHECK (stock >= 0)
    -- El stock del producto no puede ser negativo
);
Query OK, 0 rows affected (0.03 sec)

DESCRIBE productos;
+---------------+---------------+------+-----+---------+----------------+
| Field         | Type          | Null | Key | Default | Extra          |
+---------------+---------------+------+-----+---------+----------------+
| identificador | int           | NO   | PRI | NULL    | auto_increment |
| nombre        | varchar(255)  | NO   |     | NULL    |                |
| descripcion   | text          | YES  |     | NULL    |                |
| precio        | decimal(7,2)  | NO   |     | NULL    |                |
| stock         | int           | NO   |     | NULL    |                |
+---------------+---------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)


-- 3. Insertar datos
INSERT INTO productos (nombre, descripcion, precio, stock) VALUES
('Patito Clásico', 'El patito de goma amarillo tradicional.', 3.50, 120),
('Smint', 'Caja de caramelos con forma de triángulo.', 2.50, 78);
Query OK, 2 rows affected (0.01 sec)
Records: 2  Duplicates: 0  Warnings: 0

SELECT * FROM productos;
+---------------+-----------------+----------------------------------------------+--------+-------+
| identificador | nombre          | descripcion                                  | precio | stock |
+---------------+-----------------+----------------------------------------------+--------+-------+
| 1             | Patito Clásico  | El patito de goma amarillo tradicional.      |   3.50 |   120 |
| 2             | Smint           | Caja de caramelos con forma de triángulo.    |  2.50  |    78 |
+---------------+-----------------+----------------------------------------------+--------+-------+
2 rows in set (0.00 sec)


-- Inserción incorrecta para ver si se cumplen las restricciones
INSERT INTO productos (nombre, descripcion, precio, stock)
VALUES ('Goma', 'Producto con un nombre muy corto para comprobar la restricción.', 2.50, 100);
ERROR 3819 (HY000): Check constraint 'chk_nombre_min_5' is violated.

INSERT INTO productos (nombre, descripcion, precio, stock)
VALUES ('Gomas', 'Gomas del pelo', -3.00, 40);
ERROR 3819 (HY000): Check constraint 'chk_precio_no_negativo' is violated.

