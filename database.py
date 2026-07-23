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
    

def add_vehicle(vehicle):
    """
    Guarda un vehículo en la base de datos.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO vehicles (
            brand,
            model,
            year,
            license_plate,
            kilometers
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        vehicle.brand,
        vehicle.model,
        vehicle.year,
        vehicle.license_plate,
        vehicle.kilometers
    ))

    connection.commit()
    connection.close()

def get_all_vehicles():
    """
    Devuelve todos los vehículos de la base de datos.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            brand,
            model,
            year,
            license_plate,
            kilometers
        FROM vehicles
    """)

    vehicles = cursor.fetchall()

    connection.close()

    return vehicles

def update_vehicle(vehicle_id, brand, model, year, license_plate, kilometers):
    """
    Actualiza un vehículo de la base de datos.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE vehicles
        SET
            brand = ?,
            model = ?,
            year = ?,
            license_plate = ?,
            kilometers = ?
        WHERE id = ?
    """, (
        brand,
        model,
        year,
        license_plate,
        kilometers,
        vehicle_id
    ))

    connection.commit()
    connection.close()

def delete_vehicle_db(vehicle_id):
    """
    Elimina un vehículo de la base de datos.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM vehicles
        WHERE id = ?
    """, (vehicle_id,))

    connection.commit()
    connection.close()

def get_vehicle_by_license_plate(license_plate):
    """
    Busca un vehículo por su matrícula.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            brand,
            model,
            year,
            license_plate,
            kilometers
        FROM vehicles
        WHERE license_plate = ?
    """, (license_plate,))

    vehicle = cursor.fetchone()

    connection.close()

    return vehicle