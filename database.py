import sqlite3
from datetime import datetime

DATABASE_NAME = "database/autocare.db"


def get_connection():
    """
    Devuelve una conexión a la base de datos.
    """

    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row

    return connection

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
    

def add_vehicle(
    brand,
    model,
    year,
    license_plate,
    kilometers
):
    """
    Guarda un vehículo en la base de datos.
    """

    connection = get_connection()

    try:
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
            brand,
            model,
            year,
            license_plate,
            kilometers
        ))

        connection.commit()

    finally:
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

def update_vehicle(
    vehicle_id,
    brand,
    model,
    year,
    license_plate,
    kilometers
):
    """
    Actualiza un vehículo de la base de datos.
    """

    connection = get_connection()

    try:
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

    finally:
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

def add_maintenance(
    vehicle_id,
    maintenance_type,
    date,
    kilometers,
    cost,
    notes
):
    """
    Guarda un mantenimiento en la base de datos.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO maintenances (
            vehicle_id,
            maintenance_type,
            date,
            kilometers,
            cost,
            notes
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        vehicle_id,
        maintenance_type,
        date,
        kilometers,
        cost,
        notes
    ))

    connection.commit()
    connection.close()

def get_maintenances_by_vehicle(vehicle_id):
    """
    Devuelve todos los mantenimientos de un vehículo.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            maintenance_type,
            date,
            kilometers,
            cost,
            notes
        FROM maintenances
        WHERE vehicle_id = ?
        ORDER BY kilometers DESC, id DESC
    """, (vehicle_id,))

    maintenances = cursor.fetchall()

    connection.close()

    return maintenances

def update_maintenance(
    maintenance_id,
    maintenance_type,
    date,
    kilometers,
    cost,
    notes
):
    """
    Actualiza un mantenimiento.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE maintenances
            SET
                maintenance_type = ?,
                date = ?,
                kilometers = ?,
                cost = ?,
                notes = ?
            WHERE id = ?
        """, (
            maintenance_type,
            date,
            kilometers,
            cost,
            notes,
            maintenance_id
        ))

        connection.commit()

        return cursor.rowcount

    finally:
        connection.close()

def delete_maintenance_db(maintenance_id):
    """
    Elimina un mantenimiento de la base de datos.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM maintenances
            WHERE id = ?
        """, (maintenance_id,))

        connection.commit()

        return cursor.rowcount

    finally:
        connection.close()

def get_vehicle_by_id(vehicle_id):
    """
    Busca un vehículo por su identificador.
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
        WHERE id = ?
    """, (vehicle_id,))

    vehicle = cursor.fetchone()

    connection.close()

    return vehicle

def delete_vehicle(vehicle_id):
    """
    Elimina un vehículo de la base de datos.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM vehicles
            WHERE id = ?
        """, (vehicle_id,))

        connection.commit()

    finally:
        connection.close()

def get_maintenance_statistics(vehicle_id):
    """
    Devuelve las estadísticas de mantenimiento de un vehículo.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            date,
            cost
        FROM maintenances
        WHERE vehicle_id = ?
    """, (vehicle_id,))

    maintenances = cursor.fetchall()

    connection.close()

    total_cost = 0
    current_year_cost = 0
    maintenance_count = len(maintenances)

    current_year = datetime.now().year

    for maintenance in maintenances:

        cost = float(maintenance["cost"] or 0)

        total_cost += cost

        try:
            date = datetime.strptime(
                maintenance["date"],
                "%d/%m/%Y"
            )

            if date.year == current_year:
                current_year_cost += cost

        except ValueError:
            continue

    monthly_average = current_year_cost / 12

    return {
        "total_cost": round(total_cost, 2),
        "current_year_cost": round(current_year_cost, 2),
        "monthly_average": round(monthly_average, 2),
        "maintenance_count": maintenance_count
    }