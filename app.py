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
            print("Has elegido registrar vehículo")
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