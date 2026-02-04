CREATE TABLE facturas (
    id_factura INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_cliente INTEGER NOT NULL,
    total REAL DEFAULT 0,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);