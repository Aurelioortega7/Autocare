import re
from datetime import datetime


def validate_license_plate(license_plate):
    pattern = r"^\d{4}[A-Z]{3}$"
    return re.match(pattern, license_plate.upper()) is not None


def validate_year(year):
    current_year = datetime.now().year
    return 1900 <= year <= current_year


def validate_kilometers(kilometers):
    return kilometers >= 0


def validate_date(date):

    try:
        maintenance_date = datetime.strptime(date, "%d/%m/%Y")
        today = datetime.today()

        return maintenance_date <= today

    except ValueError:
        return False


def validate_cost(cost):

    return cost >= 0