from device import add_device, search_device, update_status
from engineer import add_engineer, view_engineers
from maintenance import add_maintenance, view_maintenance


try:
    while True:

        print("\n===== NETWORK DEVICE MONITORING SYSTEM =====")
        print("1. Add Engineer")
        print("2. View Engineers")
        print("3. Add Device")
        print("4. Search Device")
        print("5. Update Device Status")
        print("6. Add Maintenance")
        print("7. View Maintenance")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_engineer()

        elif choice == "2":
            view_engineers()

        elif choice == "3":
            add_device()

        elif choice == "4":
            search_device()

        elif choice == "5":
            update_status()

        elif choice == "6":
            add_maintenance()

        elif choice == "7":
            view_maintenance()

        elif choice == "8":
            print("Thank you!")
            break

        else:
            print("Invalid choice! Please select 1 to 8.")

except Exception as e:
    print("An error occurred:", e)
