import sqlite3

DATABASE_NAME = "database/autocare.db"


def get_connection():
    """
    Devuelve una conexión a la base de datos.
    """
    return sqlite3.connect(DATABASE_NAME)