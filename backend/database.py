import psycopg2
import os
from datetime import datetime

def get_connection():
    # Estas variables las cogerá del archivo .env que tienes en la EC2
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT", "5432")
    )

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    # Usamos nombres claros: busqueda y respuesta
    cur.execute("""
        CREATE TABLE IF NOT EXISTS pokedex (
            id SERIAL PRIMARY KEY,
            busqueda TEXT,
            respuesta TEXT,
            hora_busqueda TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def save_query(term, response):
    conn = get_connection()
    cur = conn.cursor()
    # Los nombres aquí deben coincidir con los de arriba (busqueda, respuesta)
    cur.execute(
        "INSERT INTO pokedex (busqueda, respuesta) VALUES (%s, %s)",
        (term, response)
    )
    conn.commit()
    cur.close()
    conn.close()
