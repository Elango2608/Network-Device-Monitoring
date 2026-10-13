from database import connect_db


def get_status():
    print("1. Active")
    print("2. Inactive")
    print("3. Maintenance")

    choice = input("Enter status: ")

    if choice == "1":
        return "Active"
    elif choice == "2":
        return "Inactive"
    elif choice == "3":
        return "Maintenance"
    else:
        return None


def add_device():
    try:
        name = input("Enter device name: ")
        device_type = input("Enter device type: ")
        ip = input("Enter IP address: ")

        status = get_status()

        if status is None:
            print("Invalid status!")
            return

        location_id = int(input("Enter location ID: "))
        engineer_id = int(input("Enter engineer ID: "))

        db = connect_db()
        cursor = db.cursor()

        query = """
        INSERT INTO devices
        (device_name, device_type, ip_address, status,
         location_id, engineer_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            name, device_type, ip,
            status, location_id, engineer_id
        )

        cursor.execute(query, values)
        db.commit()

        print("Device registered successfully!")

        cursor.close()
        db.close()

    except ValueError:
        print("Please enter valid numbers for ID.")

    except Exception as e:
        print("Error:", e)


def search_device():
    try:
        keyword = input("Enter device name: ")

        db = connect_db()
        cursor = db.cursor()

        query = """
        SELECT device_id, device_name, device_type,
               ip_address, status
        FROM devices
        WHERE device_name LIKE %s
        """

        cursor.execute(query, ("%" + keyword + "%",))
        records = cursor.fetchall()

        if records:
            for row in records:
                print(row)
        else:
            print("No device found.")

        cursor.close()
        db.close()

    except Exception as e:
        print("Error:", e)


def update_status():
    try:
        device_id = int(input("Enter device ID: "))

        status = get_status()

        if status is None:
            print("Invalid status!")
            return

        db = connect_db()
        cursor = db.cursor()

        query = """
        UPDATE devices
        SET status = %s
        WHERE device_id = %s
        """

        cursor.execute(query, (status, device_id))
        db.commit()

        if cursor.rowcount > 0:
            print("Status updated successfully!")
        else:
            print("Device not found.")

        cursor.close()
        db.close()

    except ValueError:
        print("Device ID must be a number.")

    except Exception as e:
        print("Error:", e)