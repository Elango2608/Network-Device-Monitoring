from database import connect_db


def add_maintenance():
    try:
        device_id = int(input("Enter device ID: "))
        engineer_id = int(input("Enter engineer ID: "))

        maintenance_date = input("Enter maintenance date (YYYY-MM-DD): ")
        description = input("Enter maintenance description: ")

        db = connect_db()
        cursor = db.cursor()

        query = """
        INSERT INTO maintenance
        (device_id, maintenance_date, description, engineer_id)
        VALUES (%s, %s, %s, %s)
        """

        values = (
            device_id,
            maintenance_date,
            description,
            engineer_id
        )

        cursor.execute(query, values)
        db.commit()

        print("Maintenance record added successfully!")

        cursor.close()
        db.close()

    except ValueError:
        print("Device ID and Engineer ID must be numbers.")

    except Exception as e:
        print("Error adding maintenance:", e)


def view_maintenance():
    try:
        db = connect_db()
        cursor = db.cursor()

        query = """
        SELECT
            m.maintenance_id,
            d.device_name,
            m.maintenance_date,
            m.description,
            e.engineer_name
        FROM maintenance m
        JOIN devices d
            ON m.device_id = d.device_id
        JOIN engineers e
            ON m.engineer_id = e.engineer_id
        """

        cursor.execute(query)
        records = cursor.fetchall()

        print("\n===== MAINTENANCE RECORDS =====")

        if records:
            for row in records:
                print(row)
        else:
            print("No maintenance records found.")

        cursor.close()
        db.close()

    except Exception as e:
        print("Error viewing maintenance:", e)