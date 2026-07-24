import sqlite3
from datetime import datetime, timedelta
from database import (
    initialize_database,
    add_vehicle,
    get_all_vehicles,
    update_vehicle,
    delete_vehicle_db,
    get_vehicle_by_license_plate,
    add_maintenance,
    get_maintenances_by_vehicle,
    update_maintenance,
    delete_maintenance_db
)

from validators import (
    validate_license_plate, 
    validate_year,
    validate_kilometers,
    validate_date,
    validate_cost
)

ITV_VALIDITY_DAYS = 365

initialize_database()


MAINTENANCE_TYPES = [
    "Cambio de aceite",
    "ITV",
    "Frenos",
    "Neumáticos",
    "Batería",
    "Filtros",
    "Otro"
]

def register_vehicle():
    """
    Solicita al usuario los datos de un vehículo.
    """

    print("\n===== Registrar vehículo =====")

    brand = input("Marca: ").strip().upper()
    model = input("Modelo: ").strip().upper()

    while True:
        try:
            year = int(input("Año: "))

            if validate_year(year):
                break

            print(f"El año debe estar entre 1900 y {datetime.now().year}.")

        except ValueError:
            print("Debes introducir un año válido.")

    while True:
        license_plate = input("Matrícula: ").strip().upper()

        if validate_license_plate(license_plate):
            break

        print("Matrícula no válida. Debe tener el formato 1234ABC.")

    while True:
        try:
            kilometers = int(input("Kilómetros: "))

            if validate_kilometers(kilometers):
                break

            print("Los kilómetros no pueden ser negativos.")

        except ValueError:
            print("Debes introducir un número válido.")

    try:
        add_vehicle(
            brand,
            model,
            year,
            license_plate,
            kilometers
        )

        print("\nVehículo registrado correctamente.")

    except sqlite3.IntegrityError:
        print("\nYa existe un vehículo con esa matrícula.")

def show_vehicles():
    """
    Muestra todos los vehículos registrados.
    """

    vehicles = get_all_vehicles()

    if not vehicles:
        print("\nNo hay vehículos registrados.")
        return

    print("\n===== Vehículos registrados =====")

    for index, vehicle in enumerate(vehicles, start=1):
        print(f"\nVehículo {index}")
        print(f"Marca: {vehicle['brand']}")
        print(f"Modelo: {vehicle['model']}")
        print(f"Año: {vehicle['year']}")
        print(f"Matrícula: {vehicle['license_plate']}")
        print(f"Kilómetros: {vehicle['kilometers']} km")

def delete_vehicle():
    """
    Elimina un vehículo registrado.
    """

    vehicles = get_all_vehicles()

    if not vehicles:
        print("\nNo hay vehículos para eliminar.")
        return

    show_vehicles()

    try:
        vehicle_number = int(input("\nIntroduce el número del vehículo a eliminar: "))
        index = vehicle_number - 1

        if index < 0 or index >= len(vehicles):
            print("Número de vehículo no válido.")
            return

        vehicle = vehicles[index]

        vehicle_id = vehicle["id"]
        brand = vehicle["brand"]
        model = vehicle["model"]

        while True:
            confirmation = input(
                f"\n¿Seguro que quieres eliminar {brand} {model}? (S/N): "
            ).strip().upper()

            if confirmation in ("S", "N"):
                break

            print("Introduce únicamente S o N.")

        if confirmation == "N":
            print("\nOperación cancelada.")
            return

        delete_vehicle_db(vehicle_id)

        print(f"\nVehículo eliminado: {brand} {model}")

    except ValueError:
        print("Debes introducir un número válido.")

def show_menu():
    print("\n===== AutoCare =====")
    print("1. Registrar vehículo")
    print("2. Ver vehículos")
    print("3. Editar vehículo")
    print("4. Eliminar vehículo")
    print("----------------------------")
    print("5. Registrar mantenimiento")
    print("6. Ver historial de mantenimientos")
    print("7. Editar mantenimiento")
    print("8. Eliminar mantenimiento")
    print("----------------------------")
    print("9. Estadísticas generales")
    print("10. Estadísticas de un vehículo")
    print("11. Buscar vehículo por matrícula")
    print("----------------------------")
    print("12. Estado cambio de aceite")
    print("13. Estado ITV")
    print("14. Estado frenos")
    print("15. Estado neumáticos")
    print("16. Estado batería")
    print("17. Estado filtros")
    print("----------------------------")
    print("18. Salir")

def edit_vehicle():
    """
    Permite editar los datos de un vehículo registrado.
    """

    vehicles = get_all_vehicles()

    if not vehicles:
        print("\nNo hay vehículos registrados.")
        return

    show_vehicles()

    try:
        vehicle_number = int(input("\nIntroduce el número del vehículo a editar: "))
        index = vehicle_number - 1

        if index < 0 or index >= len(vehicles):
            print("Número de vehículo no válido.")
            return

        vehicle = vehicles[index]

        vehicle_id = vehicle["id"]
        brand = vehicle["brand"]
        model = vehicle["model"]
        year = vehicle["year"]
        license_plate = vehicle["license_plate"]
        kilometers = vehicle["kilometers"]

        print("\n===== Editar vehículo =====")

        new_brand = input(f"Nueva marca [{brand}]: ").strip().upper()
        if new_brand == "":
            new_brand = brand

        new_model = input(f"Nuevo modelo [{model}]: ").strip().upper()
        if new_model == "":
            new_model = model

        while True:
            new_year = input(f"Nuevo año [{year}]: ").strip()

            if new_year == "":
                new_year = year
                break

            try:
                new_year = int(new_year)

                if validate_year(new_year):
                    break

                print(f"El año debe estar entre 1900 y {datetime.now().year}.")

            except ValueError:
                print("Debes introducir un año válido.")

        while True:
            new_license_plate = input(
                f"Nueva matrícula [{license_plate}]: "
            ).strip().upper()

            if new_license_plate == "":
                new_license_plate = license_plate
                break

            if validate_license_plate(new_license_plate):
                break

            print("Matrícula no válida. Debe tener el formato 1234ABC.")

        while True:
            new_kilometers = input(
                f"Nuevos kilómetros [{kilometers}]: "
            ).strip()

            if new_kilometers == "":
                new_kilometers = kilometers
                break

            try:
                new_kilometers = int(new_kilometers)

                if validate_kilometers(new_kilometers):
                    break

                print("Los kilómetros no pueden ser negativos.")

            except ValueError:
                print("Debes introducir un número válido.")

        try:
            update_vehicle(
                vehicle_id,
                new_brand,
                new_model,
                new_year,
                new_license_plate,
                new_kilometers
            )

            print("\nVehículo actualizado correctamente.")

        except sqlite3.IntegrityError:
            print("\nYa existe un vehículo con esa matrícula.")

    except ValueError:
        print("Debes introducir un número válido.")

def register_maintenance():
    """
    Registra un mantenimiento para un vehículo.
    """

    vehicles = get_all_vehicles()

    if not vehicles:
        print("\nNo hay vehículos registrados.")
        return

    show_vehicles()

    try:
        vehicle_number = int(input("\nSelecciona el vehículo: "))
        index = vehicle_number - 1

        if index < 0 or index >= len(vehicles):
            print("Número de vehículo no válido.")
            return

        vehicle = vehicles[index]
        vehicle_id = vehicle["id"]

        print("\n===== Registrar mantenimiento =====")

        print("\nTipos de mantenimiento:")

        for i, maintenance_type in enumerate(MAINTENANCE_TYPES, start=1):
            print(f"{i}. {maintenance_type}")

        option = int(input("\nSelecciona un tipo de mantenimiento: "))

        if option < 1 or option > len(MAINTENANCE_TYPES):
            print("Opción no válida.")
            return

        maintenance_type = MAINTENANCE_TYPES[option - 1]

        while True:
            date = input("Fecha (dd/mm/aaaa): ").strip()

            if validate_date(date):
                break

            print("La fecha no es válida. Debe tener el formato dd/mm/aaaa.")

        while True:
            try:
                kilometers = int(input("Kilómetros: "))

                if validate_kilometers(kilometers):
                    break

                print("Los kilómetros no pueden ser negativos.")

            except ValueError:
                print("Debes introducir un número válido.")

        while True:
            try:
                cost = float(input("Coste (€): "))

                if validate_cost(cost):
                    break

                print("El coste no puede ser negativo.")

            except ValueError:
                print("Debes introducir un coste válido.")

        notes = input("Observaciones: ").strip()

        add_maintenance(
            vehicle_id,
            maintenance_type,
            date,
            kilometers,
            cost,
            notes
        )

        print("\nMantenimiento registrado correctamente.")

    except ValueError:
        print("Debes introducir un valor válido.")

def show_maintenance_history():
    """
    Muestra el historial de mantenimientos de un vehículo.
    """

    vehicles = get_all_vehicles()

    if not vehicles:
        print("\nNo hay vehículos registrados.")
        return

    show_vehicles()

    try:
        vehicle_number = int(input("\nSelecciona el vehículo: "))
        index = vehicle_number - 1

        if index < 0 or index >= len(vehicles):
            print("Número de vehículo no válido.")
            return

        vehicle = vehicles[index]
        vehicle_id = vehicle["id"]

        maintenances = get_maintenances_by_vehicle(vehicle_id)

        if not maintenances:
            print("\nEste vehículo no tiene mantenimientos registrados.")
            return

        print(f"\n===== Historial de {vehicle['brand']} {vehicle['model']} =====")

        for i, maintenance in enumerate(maintenances, start=1):
            print(f"\nMantenimiento {i}")
            print(f"Tipo: {maintenance['maintenance_type']}")
            print(f"Fecha: {maintenance['date']}")
            print(f"Kilómetros: {maintenance['kilometers']} km")
            print(f"Coste: {maintenance['cost']:.2f} €")
            print(f"Observaciones: {maintenance['notes']}")

    except ValueError:
        print("Debes introducir un número válido.")


def show_total_cost():
    """
    Muestra el gasto total en mantenimientos de un vehículo.
    """

    vehicles = get_all_vehicles()

    if not vehicles:
        print("\nNo hay vehículos registrados.")
        return

    show_vehicles()

    try:
        vehicle_number = int(input("\nSelecciona el vehículo: "))
        index = vehicle_number - 1

        if index < 0 or index >= len(vehicles):
            print("Número de vehículo no válido.")
            return

        vehicle = vehicles[index]

        maintenances = get_maintenances_by_vehicle(vehicle["id"])

        total_cost = 0

        for maintenance in maintenances:
            total_cost += maintenance["cost"]

        print("\n===== Gasto total =====")
        print(f"{vehicle['brand']} {vehicle['model']}")
        print(f"Gasto acumulado: {total_cost:.2f} €")

    except ValueError:
        print("Debes introducir un número válido.")

def edit_maintenance():
    """
    Permite editar un mantenimiento registrado de un vehículo.
    """

    vehicles = get_all_vehicles()

    if not vehicles:
        print("\nNo hay vehículos registrados.")
        return

    show_vehicles()

    try:
        vehicle_number = int(input("\nSelecciona el vehículo: "))
        vehicle_index = vehicle_number - 1

        if vehicle_index < 0 or vehicle_index >= len(vehicles):
            print("Número de vehículo no válido.")
            return

        vehicle = vehicles[vehicle_index]
        vehicle_id = vehicle["id"]

        maintenances = get_maintenances_by_vehicle(vehicle_id)

        if not maintenances:
            print("\nEste vehículo no tiene mantenimientos registrados.")
            return

        print(f"\n===== Mantenimientos de {vehicle['brand']} {vehicle['model']} =====")

        for i, maintenance in enumerate(maintenances, start=1):
            print(f"\nMantenimiento {i}")
            print(f"Tipo: {maintenance['maintenance_type']}")
            print(f"Fecha: {maintenance['date']}")
            print(f"Kilómetros: {maintenance['kilometers']} km")
            print(f"Coste: {maintenance['cost']:.2f} €")

        maintenance_number = int(input("\nSelecciona el mantenimiento a editar: "))
        maintenance_index = maintenance_number - 1

        if maintenance_index < 0 or maintenance_index >= len(maintenances):
            print("Número de mantenimiento no válido.")
            return

        maintenance = maintenances[maintenance_index]

        maintenance_id = maintenance["id"]
        maintenance_type = maintenance["maintenance_type"]
        date = maintenance["date"]
        kilometers = maintenance["kilometers"]
        cost = maintenance["cost"]
        notes = maintenance["notes"]

        print("\n===== Editar mantenimiento =====")

        print("\nTipos de mantenimiento:")

        for i, m_type in enumerate(MAINTENANCE_TYPES, start=1):
            print(f"{i}. {m_type}")

        current_type = MAINTENANCE_TYPES.index(maintenance_type) + 1

        while True:
            option = input(
                f"\nSelecciona un tipo [{current_type} - {maintenance_type}]: "
            ).strip()

            if option == "":
                break

            try:
                option = int(option)

                if 1 <= option <= len(MAINTENANCE_TYPES):
                    maintenance_type = MAINTENANCE_TYPES[option - 1]
                    break

                print("Opción no válida.")

            except ValueError:
                print("Debes introducir un número válido.")

        while True:
            new_date = input(f"Nueva fecha [{date}]: ").strip()

            if new_date == "":
                break

            if validate_date(new_date):
                date = new_date
                break

            print("La fecha no es válida o es posterior a la fecha actual.")

        while True:
            new_kilometers = input(
                f"Nuevos kilómetros [{kilometers}]: "
            ).strip()

            if new_kilometers == "":
                break

            try:
                new_kilometers = int(new_kilometers)

                if validate_kilometers(new_kilometers):
                    kilometers = new_kilometers
                    break

                print("Los kilómetros no pueden ser negativos.")

            except ValueError:
                print("Debes introducir un número válido.")

        while True:
            new_cost = input(f"Nuevo coste (€) [{cost}]: ").strip()

            if new_cost == "":
                break

            try:
                new_cost = float(new_cost)

                if validate_cost(new_cost):
                    cost = new_cost
                    break

                print("El coste no puede ser negativo.")

            except ValueError:
                print("Debes introducir un coste válido.")

        new_notes = input(f"Nuevas observaciones [{notes}]: ").strip()

        if new_notes != "":
            notes = new_notes

        update_maintenance(
            maintenance_id,
            maintenance_type,
            date,
            kilometers,
            cost,
            notes
        )

        print("\nMantenimiento actualizado correctamente.")

    except ValueError:
        print("Debes introducir un valor válido.")

def delete_maintenance():
    """
    Elimina un mantenimiento de un vehículo.
    """

    vehicles = get_all_vehicles()

    if not vehicles:
        print("\nNo hay vehículos registrados.")
        return

    show_vehicles()

    try:
        vehicle_number = int(input("\nSelecciona el vehículo: "))
        vehicle_index = vehicle_number - 1

        if vehicle_index < 0 or vehicle_index >= len(vehicles):
            print("Número de vehículo no válido.")
            return

        vehicle = vehicles[vehicle_index]
        vehicle_id = vehicle["id"]

        maintenances = get_maintenances_by_vehicle(vehicle_id)

        if not maintenances:
            print("\nEste vehículo no tiene mantenimientos registrados.")
            return

        print(f"\n===== Mantenimientos de {vehicle['brand']} {vehicle['model']} =====")

        for i, maintenance in enumerate(maintenances, start=1):
            print(f"\nMantenimiento {i}")
            print(f"Tipo: {maintenance['maintenance_type']}")
            print(f"Fecha: {maintenance['date']}")
            print(f"Kilómetros: {maintenance['kilometers']} km")
            print(f"Coste: {maintenance['cost']:.2f} €")

        maintenance_number = int(input("\nSelecciona el mantenimiento a eliminar: "))
        maintenance_index = maintenance_number - 1

        if maintenance_index < 0 or maintenance_index >= len(maintenances):
            print("Número de mantenimiento no válido.")
            return

        maintenance = maintenances[maintenance_index]

        while True:
            confirmation = input(
                f"\n¿Seguro que quieres eliminar el mantenimiento "
                f"'{maintenance['maintenance_type']}'? (S/N): "
            ).strip().upper()

            if confirmation in ("S", "N"):
                break

            print("Introduce únicamente S o N.")

        if confirmation == "N":
            print("\nOperación cancelada.")
            return

        delete_maintenance_db(maintenance["id"])

        print(
            f"\nSe ha eliminado el mantenimiento "
            f"'{maintenance['maintenance_type']}' correctamente."
        )

    except ValueError:
        print("Debes introducir un valor válido.")

def search_vehicle_by_license_plate():
    """
    Busca un vehículo por su matrícula.
    """

    license_plate = input("\nIntroduce la matrícula: ").strip().upper()

    vehicle = get_vehicle_by_license_plate(license_plate)

    if vehicle is None:
        print("\nNo se ha encontrado ningún vehículo con esa matrícula.")
        return

    print("\n===== Vehículo encontrado =====")
    print(f"Marca: {vehicle['brand']}")
    print(f"Modelo: {vehicle['model']}")
    print(f"Año: {vehicle['year']}")
    print(f"Matrícula: {vehicle['license_plate']}")
    print(f"Kilómetros: {vehicle['kilometers']} km")

def show_statistics():
    """
    Muestra estadísticas generales de AutoCare.
    """

    vehicles = get_all_vehicles()

    if not vehicles:
        print("\nNo hay vehículos registrados.")
        return

    total_vehicles = len(vehicles)
    total_maintenances = 0
    total_cost = 0

    vehicle_with_most_maintenances = None
    max_maintenances = 0

    vehicle_with_highest_cost = None
    highest_cost = 0

    for vehicle in vehicles:

        maintenances = get_maintenances_by_vehicle(vehicle["id"])

        num_maintenances = len(maintenances)
        total_maintenances += num_maintenances

        vehicle_cost = 0

        for maintenance in maintenances:
            vehicle_cost += maintenance["cost"]

        total_cost += vehicle_cost

        if num_maintenances > max_maintenances:
            max_maintenances = num_maintenances
            vehicle_with_most_maintenances = vehicle

        if vehicle_cost > highest_cost:
            highest_cost = vehicle_cost
            vehicle_with_highest_cost = vehicle

    average_cost = total_cost / total_vehicles

    print("\n===== Estadísticas generales =====")
    print(f"Vehículos registrados: {total_vehicles}")
    print(f"Mantenimientos registrados: {total_maintenances}")
    print(f"Gasto total: {total_cost:.2f} €")
    print(f"Gasto medio por vehículo: {average_cost:.2f} €")

    if vehicle_with_most_maintenances:
        print(
            f"Vehículo con más mantenimientos: "
            f"{vehicle_with_most_maintenances['brand']} "
            f"{vehicle_with_most_maintenances['model']}"
        )

    if vehicle_with_highest_cost:
        print(
            f"Vehículo con mayor gasto: "
            f"{vehicle_with_highest_cost['brand']} "
            f"{vehicle_with_highest_cost['model']}"
        )

def show_vehicle_statistics():
    """
    Muestra estadísticas de un vehículo.
    """

    vehicles = get_all_vehicles()

    if not vehicles:
        print("\nNo hay vehículos registrados.")
        return

    show_vehicles()

    try:

        vehicle_number = int(input("\nSelecciona un vehículo: "))
        vehicle_index = vehicle_number - 1

        if vehicle_index < 0 or vehicle_index >= len(vehicles):
            print("Número de vehículo no válido.")
            return

        vehicle = vehicles[vehicle_index]

        maintenances = get_maintenances_by_vehicle(vehicle["id"])

        total_cost = 0

        for maintenance in maintenances:
            total_cost += maintenance["cost"]

        total_maintenances = len(maintenances)

        average_cost = 0

        if total_maintenances > 0:
            average_cost = total_cost / total_maintenances

        print("\n===== Estadísticas del vehículo =====")
        print(f"Marca: {vehicle['brand']}")
        print(f"Modelo: {vehicle['model']}")
        print(f"Año: {vehicle['year']}")
        print(f"Matrícula: {vehicle['license_plate']}")
        print(f"Kilómetros: {vehicle['kilometers']} km")
        print(f"Mantenimientos: {total_maintenances}")
        print(f"Gasto total: {total_cost:.2f} €")
        print(f"Coste medio: {average_cost:.2f} €")

        if total_maintenances > 0:
            last = maintenances[0]

            print("\nÚltimo mantenimiento")
            print(f"Tipo: {last['maintenance_type']}")
            print(f"Fecha: {last['date']}")
            print(f"Coste: {last['cost']:.2f} €")

    except ValueError:
        print("Debes introducir un número válido.")

def maintenance_reminder(
    maintenance_type,
    title,
    warning_message,
    urgent_message,
    missing_message,
    max_km=None,
    max_days=None
):
    """
    Comprueba el estado de un tipo de mantenimiento.
    """

    vehicles = get_all_vehicles()

    if not vehicles:
        print("\nNo hay vehículos registrados.")
        return

    show_vehicles()

    try:
        vehicle_number = int(input("\nSelecciona un vehículo: "))
        index = vehicle_number - 1

        if index < 0 or index >= len(vehicles):
            print("Número de vehículo no válido.")
            return

        vehicle = vehicles[index]

        maintenances = get_maintenances_by_vehicle(vehicle["id"])

        last_maintenance = None

        # Buscar el último mantenimiento del tipo indicado
        for maintenance in maintenances:
            if maintenance["maintenance_type"] == maintenance_type:
                last_maintenance = maintenance
                break

        if last_maintenance is None:
            print(f"\n{missing_message}")
            return

        kilometers_since = (
            vehicle["kilometers"] - last_maintenance["kilometers"]
        )

        last_date = datetime.strptime(
            last_maintenance["date"],
            "%d/%m/%Y"
        )

        today = datetime.today()

        days_since = (today - last_date).days

        print(f"\n===== Estado de {title} =====")
        print(f"Vehículo: {vehicle['brand']} {vehicle['model']}")
        print(f"Último mantenimiento: {last_maintenance['date']}")
        print(
            f"Kilómetros del mantenimiento: "
            f"{last_maintenance['kilometers']} km"
        )
        print(f"Kilómetros actuales: {vehicle['kilometers']} km")
        print(f"Kilómetros recorridos: {kilometers_since} km")
        print(f"Días transcurridos: {days_since}")

        print("\nEstado:")

        km_expired = (
            max_km is not None and
            kilometers_since >= max_km
        )

        days_expired = (
            max_days is not None and
            days_since >= max_days
        )

        if km_expired and days_expired:
            print(urgent_message)
            print("Motivos:")

            if max_km is not None:
                print(f"- Han pasado más de {max_km:,} km.".replace(",", "."))

            if max_days is not None:
                print(f"- Han pasado más de {max_days} días.")

        elif km_expired:
            print(warning_message)
            print(
                f"Motivo: Han pasado más de "
                f"{max_km:,} km.".replace(",", ".")
            )

        elif days_expired:
            print(warning_message)
            print(f"Motivo: Han pasado más de {max_days} días.")

        else:
            print(f"{title} en buen estado.")

            if max_km is not None:
                remaining_km = max_km - kilometers_since
                print(f"Quedan aproximadamente {remaining_km} km.")

            if max_days is not None:
                remaining_days = max_days - days_since
                print(f"Quedan aproximadamente {remaining_days} días.")

    except ValueError:
        print("Debes introducir un valor válido.")

def oil_change_reminder():
    """
    Comprueba el estado del cambio de aceite.
    """

    maintenance_reminder(
        maintenance_type="Cambio de aceite",
        title="Cambio de aceite",
        warning_message="Debes cambiar el aceite.",
        urgent_message="Cambio de aceite URGENTE.",
        missing_message="Este vehículo no tiene registrado ningún cambio de aceite.",
        max_km=10000,
        max_days=365
    )

def brakes_reminder():
    """
    Comprueba el estado de los frenos.
    """

    maintenance_reminder(
        maintenance_type="Frenos",
        title="Frenos",
        warning_message="Debes revisar los frenos.",
        urgent_message="Revisión de frenos URGENTE.",
        missing_message="Este vehículo no tiene registrado ningún cambio de frenos.",
        max_km=30000,
        max_days=730
    )

def tires_reminder():
    """
    Comprueba el estado de los neumáticos.
    """

    maintenance_reminder(
        maintenance_type="Neumáticos",
        title="Neumáticos",
        warning_message="Debes revisar los neumáticos.",
        urgent_message="Cambio de neumáticos URGENTE.",
        missing_message="Este vehículo no tiene registrado ningún cambio de neumáticos.",
        max_km=40000,
        max_days=1825
    )

def battery_reminder():
    """
    Comprueba el estado de la batería.
    """

    maintenance_reminder(
        maintenance_type="Batería",
        title="Batería",
        warning_message="Debes revisar la batería.",
        urgent_message="Sustitución de batería recomendada.",
        missing_message="Este vehículo no tiene registrado ningún cambio de batería.",
        max_days=1825
    )

def filters_reminder():
    """
    Comprueba el estado de los filtros.
    """

    maintenance_reminder(
        maintenance_type="Filtros",
        title="Filtros",
        warning_message="Debes cambiar los filtros.",
        urgent_message="Cambio de filtros URGENTE.",
        missing_message="Este vehículo no tiene registrado ningún cambio de filtros.",
        max_km=20000,
        max_days=365
    )

def itv_reminder():
    """
    Comprueba si la ITV está próxima a caducar o ya ha caducado.
    """

    vehicles = get_all_vehicles()

    if not vehicles:
        print("\nNo hay vehículos registrados.")
        return

    show_vehicles()

    try:
        vehicle_number = int(input("\nSelecciona un vehículo: "))
        index = vehicle_number - 1

        if index < 0 or index >= len(vehicles):
            print("Número de vehículo no válido.")
            return

        vehicle = vehicles[index]

        maintenances = get_maintenances_by_vehicle(vehicle["id"])

        last_itv = None

        # Buscar la última ITV registrada
        for maintenance in maintenances:
            if maintenance["maintenance_type"] == "ITV":
                last_itv = maintenance
                break

        if last_itv is None:
            print("\nEste vehículo no tiene ninguna ITV registrada.")
            return

        last_date = datetime.strptime(
            last_itv["date"],
            "%d/%m/%Y"
        )

        next_itv = last_date + timedelta(days=ITV_VALIDITY_DAYS)

        today = datetime.today()

        days_since = (today - last_date).days
        remaining_days = (next_itv - today).days

        print("\n===== Estado ITV =====")
        print(f"Vehículo: {vehicle['brand']} {vehicle['model']}")
        print(f"Última ITV: {last_itv['date']}")
        print(f"Días desde la última ITV: {days_since}")
        print(f"Próxima ITV: {next_itv.strftime('%d/%m/%Y')}")

        print("\nEstado:")

        if remaining_days < 0:
            print("ITV CADUCADA.")
            print(f"Caducó hace {-remaining_days} días.")

        elif remaining_days <= 30:
            print("ITV próxima a caducar.")
            print(f"Caduca en {remaining_days} días.")

        else:
            print("ITV en vigor.")
            print(
                f"Quedan {remaining_days} días "
                "para la próxima inspección."
            )

    except ValueError:
        print("Debes introducir un valor válido.")

def main():
    while True:
        show_menu()
        option = input("Elige una opción: ")

        if option == "1":
            register_vehicle()

        elif option == "2":
            show_vehicles()

        elif option == "3":
            edit_vehicle()

        elif option == "4":
            delete_vehicle()

        elif option == "5":
            register_maintenance()

        elif option == "6":
            show_maintenance_history()

        elif option == "7":
            edit_maintenance()

        elif option == "8":
            delete_maintenance()

        elif option == "9":
            show_statistics()

        elif option == "10":
            show_vehicle_statistics()

        elif option == "11":
            search_vehicle_by_license_plate()

        elif option == "12":
            oil_change_reminder()
        
        elif option == "13":
            itv_reminder()

        elif option == "14":
            brakes_reminder()

        elif option == "15":
            tires_reminder()

        elif option == "16":
            battery_reminder()

        elif option == "17":
            filters_reminder()

        elif option == "18":
            print("Saliendo de AutoCare...")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()