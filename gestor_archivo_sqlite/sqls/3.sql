CREATE TABLE IF NOT EXISTS facturas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    fecha DATE DEFAULT (date('now')),
    total REAL NOT NULL DEFAULT 0,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);
