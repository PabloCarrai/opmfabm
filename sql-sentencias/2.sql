CREATE TABLE productos (
    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL,
    precio REAL NOT NULL CHECK(precio >= 0),
    stock INTEGER NOT NULL DEFAULT 0
);