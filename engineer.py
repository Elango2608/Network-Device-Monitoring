from database import connect_db


def add_engineer():
    try:
        name = input("Enter engineer name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        db = connect_db()
        cursor = db.cursor()

        query = """
        INSERT INTO engineers
        (engineer_name, phone, email)
        VALUES (%s, %s, %s)
        """

        cursor.execute(query, (name, phone, email))
        db.commit()

        print("Engineer added successfully!")

        cursor.close()
        db.close()

    except Exception as e:
        print("Error adding engineer:", e)


def view_engineers():
    try:
        db = connect_db()
        cursor = db.cursor()

        query = "SELECT * FROM engineers"

        cursor.execute(query)
        records = cursor.fetchall()

        print("\n===== ENGINEER LIST =====")

        if records:
            for row in records:
                print(row)
        else:
            print("No engineers found.")

        cursor.close()
        db.close()

    except Exception as e:
        print("Error viewing engineers:", e)
