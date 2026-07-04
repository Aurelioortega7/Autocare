from models.vehicle import Vehicle

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

    print("\n Vehículo registrado correctamente.")
    print(f"Marca: {vehicle.brand}")
    print(f"Modelo: {vehicle.model}")
    print(f"Año: {vehicle.year}")
    print(f"Matrícula: {vehicle.license_plate}")
    print(f"Kilómetros: {vehicle.kilometers} km")

def show_menu():
    print("\n===== AutoCare =====")
    print("1. Registrar vehículo")
    print("2. Ver vehículos")
    print("3. Registrar mantenimiento")
    print("4. Ver historial")
    print("5. Salir")


def main():
    while True:
        show_menu()
        option = input("Elige una opción: ")

        if option == "1":
            register_vehicle()
        elif option == "2":
            print("Has elegido ver vehículos")
        elif option == "3":
            print("Has elegido registrar mantenimiento")
        elif option == "4":
            print("Has elegido ver historial")
        elif option == "5":
            print("Saliendo de AutoCare...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()