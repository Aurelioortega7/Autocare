from models.vehicle import Vehicle
vehicles = []

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
    print("3. Registrar mantenimiento")
    print("4. Ver historial")
    print("5. Editar vehículo")
    print("6. Eliminar vehículo")
    print("7. Salir")

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

        vehicle.brand = input("Nueva marca: ")
        vehicle.model = input("Nuevo modelo: ")
        vehicle.year = int(input("Nuevo año: "))
        vehicle.license_plate = input("Nueva matrícula: ")
        vehicle.kilometers = int(input("Nuevos kilómetros: "))

        print("\nVehículo actualizado correctamente.")

    except ValueError:
        print("Debes introducir un número válido.")

def main():
    while True:
        show_menu()
        option = input("Elige una opción: ")

        if option == "1":
            register_vehicle()
        elif option == "2":
            show_vehicles()
        elif option == "3":
            print("Has elegido registrar mantenimiento")
        elif option == "4":
            print("Has elegido ver historial")
        elif option == "5":
            edit_vehicle()
        elif option == "6":
            delete_vehicle()
        elif option == "7":
            print("Saliendo de AutoCare...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()