import sqlite3

DATABASE_NAME = "database/autocare.db"


def get_connection():
    """
    Devuelve una conexión a la base de datos.
    """
    return sqlite3.connect(DATABASE_NAME)

def initialize_database():
    """
    Crea las tablas de la base de datos si no existen.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehicles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            license_plate TEXT UNIQUE NOT NULL,
            kilometers INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS maintenances (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_id INTEGER NOT NULL,
            maintenance_type TEXT NOT NULL,
            date TEXT NOT NULL,
            kilometers INTEGER NOT NULL,
            cost REAL NOT NULL,
            notes TEXT,
            FOREIGN KEY (vehicle_id) REFERENCES vehicles(id)
        )
    """)

    connection.commit()
    connection.close()