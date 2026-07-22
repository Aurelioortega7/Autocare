from datetime import datetime, timedelta
from models.vehicle import Vehicle
from models.maintenance import Maintenance

vehicles = []
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
    Solicita al usuario los datos de un vehículo y crea un objeto Vehicle.
    """

    print("\n===== Registrar vehículo =====")

    brand = input("Marca: ")
    model = input("Modelo: ")
    year = int(input("Año: "))
    license_plate = input("Matrícula: ")
    kilometers = int(input("Kilómetros: "))

    vehicle = Vehicle(
        brand,
        model,
        year,
        license_plate,
        kilometers
    )

    vehicles.append(vehicle)

    print("\n Vehículo registrado correctamente.")

def show_vehicles():
    """
    Muestra todos los vehículos registrados durante la ejecución del programa.
    """

    if not vehicles:
        print("\nNo hay vehículos registrados.")
        return

    print("\n===== Vehículos registrados =====")

    for index, vehicle in enumerate(vehicles, start=1):
        print(f"\nVehículo {index}")
        print(f"Marca: {vehicle.brand}")
        print(f"Modelo: {vehicle.model}")
        print(f"Año: {vehicle.year}")
        print(f"Matrícula: {vehicle.license_plate}")
        print(f"Kilómetros: {vehicle.kilometers} km")

def delete_vehicle():
    """
    Elimina un vehículo registrado según su número en la lista.
    """

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

        removed_vehicle = vehicles.pop(index)
        print(f"\nVehículo eliminado: {removed_vehicle.brand} {removed_vehicle.model}")

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
    print("----------------------------")
    print("14. Salir")

def edit_vehicle():
    """
    Permite editar los datos de un vehículo registrado.
    """

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

        print("\n===== Editar vehículo =====")

        new_brand = input(f"Nueva marca [{vehicle.brand}]: ")
        if new_brand != "":
            vehicle.brand = new_brand

        new_model = input(f"Nuevo modelo [{vehicle.model}]: ")
        if new_model != "":
            vehicle.model = new_model

        new_year = input(f"Nuevo año [{vehicle.year}]: ")
        if new_year != "":
            vehicle.year = int(new_year)

        new_license_plate = input(f"Nueva matrícula [{vehicle.license_plate}]: ")
        if new_license_plate != "":
            vehicle.license_plate = new_license_plate

        new_kilometers = input(f"Nuevos kilómetros [{vehicle.kilometers}]: ")
        if new_kilometers != "":
            vehicle.kilometers = int(new_kilometers)

        print("\nVehículo actualizado correctamente.")

    except ValueError:
        print("Debes introducir un número válido.")

def register_maintenance():
    """
    Registra un mantenimiento para un vehículo.
    """

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

        print("\n===== Registrar mantenimiento =====")

        print("\nTipos de mantenimiento:")

        for i, maintenance_type in enumerate(MAINTENANCE_TYPES, start=1):
            print(f"{i}. {maintenance_type}")

        option = int(input("\nSelecciona un tipo de mantenimiento: "))

        if option < 1 or option > len(MAINTENANCE_TYPES):
            print("Opción no válida.")
            return

        maintenance_type = MAINTENANCE_TYPES[option - 1]

        date = input("Fecha (dd/mm/aaaa): ")
        kilometers = int(input("Kilómetros: "))
        cost = float(input("Coste (€): "))
        notes = input("Observaciones: ")

        maintenance = Maintenance(
            maintenance_type,
            date,
            kilometers,
            cost,
            notes
        )

        vehicle.maintenances.append(maintenance)

        print("\nMantenimiento registrado correctamente.")

    except ValueError:
        print("Debes introducir un valor válido.")

        vehicle.maintenances.append(maintenance)

        print("\nMantenimiento registrado correctamente.")

    except ValueError:
        print("Debes introducir un valor válido.")

def show_maintenance_history():
    """
    Muestra el historial de mantenimientos de un vehículo.
    """

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

        if not vehicle.maintenances:
            print("\nEste vehículo no tiene mantenimientos registrados.")
            return

        print(f"\n===== Historial de {vehicle.brand} {vehicle.model} =====")

        for i, maintenance in enumerate(vehicle.maintenances, start=1):
            print(f"\nMantenimiento {i}")
            print(f"Tipo: {maintenance.maintenance_type}")
            print(f"Fecha: {maintenance.date}")
            print(f"Kilómetros: {maintenance.kilometers} km")
            print(f"Coste: {maintenance.cost:.2f} €")
            print(f"Observaciones: {maintenance.notes}")

    except ValueError:
        print("Debes introducir un número válido.")

def show_total_cost():
    """
    Muestra el gasto total en mantenimientos de un vehículo.
    """

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

        total_cost = 0

        for maintenance in vehicle.maintenances:
            total_cost += maintenance.cost

        print(f"\n===== Gasto total =====")
        print(f"{vehicle.brand} {vehicle.model}")
        print(f"Gasto acumulado: {total_cost:.2f} €")

    except ValueError:
        print("Debes introducir un número válido.")

def edit_maintenance():
    """
    Permite editar un mantenimiento registrado de un vehículo.
    """

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

        if not vehicle.maintenances:
            print("\nEste vehículo no tiene mantenimientos registrados.")
            return

        print(f"\n===== Mantenimientos de {vehicle.brand} {vehicle.model} =====")

        for i, maintenance in enumerate(vehicle.maintenances, start=1):
            print(f"\nMantenimiento {i}")
            print(f"Tipo: {maintenance.maintenance_type}")
            print(f"Fecha: {maintenance.date}")
            print(f"Kilómetros: {maintenance.kilometers} km")
            print(f"Coste: {maintenance.cost:.2f} €")

        maintenance_number = int(input("\nSelecciona el mantenimiento a editar: "))
        maintenance_index = maintenance_number - 1

        if maintenance_index < 0 or maintenance_index >= len(vehicle.maintenances):
            print("Número de mantenimiento no válido.")
            return

        maintenance = vehicle.maintenances[maintenance_index]

        print("\n===== Editar mantenimiento =====")

        print("\nTipos de mantenimiento:")
        for i, maintenance_type in enumerate(MAINTENANCE_TYPES, start=1):
            print(f"{i}. {maintenance_type}")

        current_type = MAINTENANCE_TYPES.index(maintenance.maintenance_type) + 1

        option = input(
            f"\nSelecciona un tipo [{current_type} - {maintenance.maintenance_type}]: "
        )

        if option != "":
            option = int(option)

            if option < 1 or option > len(MAINTENANCE_TYPES):
                print("Opción no válida.")
                return

            maintenance.maintenance_type = MAINTENANCE_TYPES[option - 1]

        new_date = input(f"Nueva fecha [{maintenance.date}]: ")
        if new_date != "":
            maintenance.date = new_date

        new_kilometers = input(f"Nuevos kilómetros [{maintenance.kilometers}]: ")
        if new_kilometers != "":
            maintenance.kilometers = int(new_kilometers)

        new_cost = input(f"Nuevo coste (€) [{maintenance.cost}]: ")
        if new_cost != "":
            maintenance.cost = float(new_cost)

        new_notes = input(f"Nuevas observaciones [{maintenance.notes}]: ")
        if new_notes != "":
            maintenance.notes = new_notes

        print("\nMantenimiento actualizado correctamente.")

    except ValueError:
        print("Debes introducir un valor válido.")

def delete_maintenance():
    """
    Elimina un mantenimiento de un vehículo.
    """

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

        if not vehicle.maintenances:
            print("\nEste vehículo no tiene mantenimientos registrados.")
            return

        print(f"\n===== Mantenimientos de {vehicle.brand} {vehicle.model} =====")

        for i, maintenance in enumerate(vehicle.maintenances, start=1):
            print(f"\nMantenimiento {i}")
            print(f"Tipo: {maintenance.maintenance_type}")
            print(f"Fecha: {maintenance.date}")
            print(f"Kilómetros: {maintenance.kilometers} km")
            print(f"Coste: {maintenance.cost:.2f} €")

        maintenance_number = int(input("\nSelecciona el mantenimiento a eliminar: "))
        maintenance_index = maintenance_number - 1

        if maintenance_index < 0 or maintenance_index >= len(vehicle.maintenances):
            print("Número de mantenimiento no válido.")
            return

        deleted_maintenance = vehicle.maintenances.pop(maintenance_index)

        print(f"\nSe ha eliminado el mantenimiento '{deleted_maintenance.maintenance_type}' correctamente.")

    except ValueError:
        print("Debes introducir un valor válido.")

def search_vehicle_by_license_plate():
    """
    Busca un vehículo por su matrícula.
    """

    if not vehicles:
        print("\nNo hay vehículos registrados.")
        return

    license_plate = input("\nIntroduce la matrícula: ").strip().upper()

    for vehicle in vehicles:
        if vehicle.license_plate.upper() == license_plate:

            print("\n===== Vehículo encontrado =====")
            print(f"Marca: {vehicle.brand}")
            print(f"Modelo: {vehicle.model}")
            print(f"Año: {vehicle.year}")
            print(f"Matrícula: {vehicle.license_plate}")
            print(f"Kilómetros: {vehicle.kilometers} km")
            print(f"Mantenimientos registrados: {len(vehicle.maintenances)}")

            return

    print("\nNo se ha encontrado ningún vehículo con esa matrícula.")

def show_statistics():
    """
    Muestra estadísticas generales de AutoCare.
    """

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

        maintenances = len(vehicle.maintenances)
        total_maintenances += maintenances

        vehicle_cost = 0

        for maintenance in vehicle.maintenances:
            vehicle_cost += maintenance.cost

        total_cost += vehicle_cost

        if maintenances > max_maintenances:
            max_maintenances = maintenances
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
            f"{vehicle_with_most_maintenances.brand} "
            f"{vehicle_with_most_maintenances.model}"
        )

    if vehicle_with_highest_cost:
        print(
            f"Vehículo con mayor gasto: "
            f"{vehicle_with_highest_cost.brand} "
            f"{vehicle_with_highest_cost.model}"
        )

def show_vehicle_statistics():
    """
    Muestra estadísticas de un vehículo.
    """

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

        total_cost = 0

        for maintenance in vehicle.maintenances:
            total_cost += maintenance.cost

        total_maintenances = len(vehicle.maintenances)

        average_cost = 0

        if total_maintenances > 0:
            average_cost = total_cost / total_maintenances

        print("\n===== Estadísticas del vehículo =====")
        print(f"Marca: {vehicle.brand}")
        print(f"Modelo: {vehicle.model}")
        print(f"Año: {vehicle.year}")
        print(f"Matrícula: {vehicle.license_plate}")
        print(f"Kilómetros: {vehicle.kilometers} km")
        print(f"Mantenimientos: {total_maintenances}")
        print(f"Gasto total: {total_cost:.2f} €")
        print(f"Coste medio: {average_cost:.2f} €")

        if total_maintenances > 0:
            last = vehicle.maintenances[-1]

            print("\nÚltimo mantenimiento")
            print(f"Tipo: {last.maintenance_type}")
            print(f"Fecha: {last.date}")
            print(f"Coste: {last.cost:.2f} €")

    except ValueError:
        print("Debes introducir un número válido.")

def oil_change_reminder():
    """
    Comprueba si un vehículo necesita un cambio de aceite.
    El aviso se genera si han pasado más de 10.000 km
    o más de un año desde el último cambio.
    """

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

        last_oil_change = None

        # Buscar el último cambio de aceite
        for maintenance in reversed(vehicle.maintenances):
            if maintenance.maintenance_type == "Cambio de aceite":
                last_oil_change = maintenance
                break

        if last_oil_change is None:
            print("\nEste vehículo no tiene registrado ningún cambio de aceite.")
            return

        # Calcular kilómetros recorridos
        kilometers_since = vehicle.kilometers - last_oil_change.kilometers

        # Calcular tiempo transcurrido
        last_date = datetime.strptime(last_oil_change.date, "%d/%m/%Y")
        today = datetime.today()

        days_since = (today - last_date).days

        print("\n===== Aviso de cambio de aceite =====")
        print(f"Vehículo: {vehicle.brand} {vehicle.model}")
        print(f"Último cambio: {last_oil_change.date}")
        print(f"Kilómetros del cambio: {last_oil_change.kilometers} km")
        print(f"Kilómetros actuales: {vehicle.kilometers} km")
        print(f"Kilómetros recorridos: {kilometers_since} km")
        print(f"Días transcurridos: {days_since}")

        print("\nEstado:")

        if kilometers_since >= 10000 and days_since >= 365:
            print("Cambio de aceite URGENTE.")
            print("Motivos:")
            print("- Han pasado más de 10.000 km.")
            print("- Ha pasado más de un año.")

        elif kilometers_since >= 10000:
            print("Debes cambiar el aceite.")
            print("Motivo: Han pasado más de 10.000 km.")

        elif days_since >= 365:
            print("Debes cambiar el aceite.")
            print("Motivo: Ha pasado más de un año.")

        else:
            remaining_km = 10000 - kilometers_since
            remaining_days = 365 - days_since

            print("El cambio de aceite no es necesario todavía.")
            print(f"Quedan aproximadamente {remaining_km} km.")
            print(f"Quedan aproximadamente {remaining_days} días.")

    except ValueError:
        print("Debes introducir un valor válido.")

def itv_reminder():
    """
    Comprueba si la ITV está próxima a caducar o ya ha caducado.
    """

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

        last_itv = None

        # Buscar la última ITV registrada
        for maintenance in reversed(vehicle.maintenances):
            if maintenance.maintenance_type == "ITV":
                last_itv = maintenance
                break

        if last_itv is None:
            print("\nEste vehículo no tiene ninguna ITV registrada.")
            return

        last_date = datetime.strptime(last_itv.date, "%d/%m/%Y")
        next_itv = last_date + timedelta(days=365)

        today = datetime.today()
        remaining_days = (next_itv - today).days

        print("\n===== Aviso ITV =====")
        print(f"Vehículo: {vehicle.brand} {vehicle.model}")
        print(f"Última ITV: {last_itv.date}")
        print(f"Próxima ITV: {next_itv.strftime('%d/%m/%Y')}")

        if remaining_days < 0:
            print(f"\nLa ITV ha caducado hace {-remaining_days} días.")

        elif remaining_days <= 30:
            print(f"\nLa ITV caduca en {remaining_days} días.")

        else:
            print(f"\nLa ITV está en vigor.")
            print(f"Quedan {remaining_days} días.")
            
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
            print("Saliendo de AutoCare...")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()