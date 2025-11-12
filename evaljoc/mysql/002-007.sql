sudo mysql -u root -p

USE empresadam;
Database changed

SHOW TABLES;
+------------------+
| Tables_in_empresadam |
+------------------+
| clientes         |
| productos        |
+------------------+
2 rows in set (0.00 sec)

CREATE TABLE pedidos (
  numerodepedido VARCHAR(20) NOT NULL,
  cliente VARCHAR(50) NOT NULL,
  producto VARCHAR(255) NOT NULL
);
Query OK, 0 rows affected (0.01 sec)

INSERT INTO pedidos (numerodepedido, cliente, producto) VALUES
('P1', 'Sam Pérez', 'Manta');
Query OK, 1 row affected (0.00 sec)

INSERT INTO pedidos (numerodepedido, cliente, producto) VALUES
('P2', NULL, 'Impresora');
ERROR 1048 (23000): Column 'cliente' cannot be null

SELECT * FROM pedidos;
+---------------+------------+----------+
| numerodepedido| cliente    | producto |
+---------------+------------+----------+
| P1            | Sam Pérez  | Manta    |
+---------------+------------+----------+
