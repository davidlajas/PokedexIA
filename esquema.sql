CREATE TABLE pokedex (
    id SERIAL PRIMARY KEY,
    pregunta TEXT NOT NULL,
    respuesta TEXT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);