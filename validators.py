import re
from datetime import datetime

def validate_license_plate(license_plate):
    """
    Comprueba que la matrícula tenga el formato español 1234ABC.
    """

    pattern = r"^\d{4}[A-Z]{3}$"

    return re.match(pattern, license_plate.upper()) is not None

def validate_year(year):
    """
    Comprueba que el año del vehículo sea válido.
    """

    current_year = datetime.now().year

    return 1900 <= year <= current_year

def validate_kilometers(kilometers):
    """
    Comprueba que los kilómetros sean válidos.
    """

    return kilometers >= 0