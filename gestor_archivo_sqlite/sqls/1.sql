CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    telefono TEXT,
    email TEXT UNIQUE,
    fecha_alta DATE DEFAULT (date('now')),
    activo INTEGER DEFAULT 1
);
