import mysql.connector as mycon

def create_connection():
    """Establish a connection to the MySQL database."""
    try:
        connection = mycon.connect(
            host='localhost',
            user='root',
            password='user',  # Replace with your MySQL root password
            database='hospital'  # Ensure the database name is correct
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except mycon.Error as err:
        print(f"Error: {err}")
        return None

def setup_database(connection):
    """Create database and table if they do not exist."""
    try:
        cursor = connection.cursor()
        # Create database if not exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS hospital")
        cursor.execute("USE hospital")
        # Create table if not exists
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            age INT,
            gender VARCHAR(10),
            address VARCHAR(100),
            phone VARCHAR(20)
        )
        """)
        connection.commit()
        print("Database and table setup completed successfully")
    except mycon.Error as err:
        print(f"Error: {err}")

def add_patient(connection):
    """Add a new patient record to the database."""
    try:
        cursor = connection.cursor()
        name = input("Enter Patient Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        address = input("Enter Address: ")
        phone = input("Enter Phone Number: ")

        query = "INSERT INTO patients (name, age, gender, address, phone) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (name, age, gender, address, phone))
        connection.commit()
        print("## Data Saved ##")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except mycon.Error as err:
        print(f"Database Error: {err}")

def delete_patient(connection):
    """Delete a patient record from the database by ID."""
    try:
        cursor = connection.cursor()
        patient_id = int(input("Enter Patient ID to delete: "))
        query = "DELETE FROM patients WHERE patient_id = %s"
        cursor.execute(query, (patient_id,))
        connection.commit()
        if cursor.rowcount > 0:
            print("## Patient Deleted ##")
        else:
            print("## Patient ID not found ##")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except mycon.Error as err:
        print(f"Database Error: {err}")

def update_patient(connection):
    """Update a patient's details in the database."""
    try:
        cursor = connection.cursor()
        patient_id = int(input("Enter Patient ID to update: "))
        name = input("Enter new Patient Name: ")
        age = int(input("Enter new Age: "))
        gender = input("Enter new Gender: ")
        address = input("Enter new Address: ")
        phone = input("Enter new Phone Number: ")

        query = """
        UPDATE patients
        SET name = %s, age = %s, gender = %s, address = %s, phone = %s
        WHERE patient_id = %s
        """
        cursor.execute(query, (name, age, gender, address, phone, patient_id))
        connection.commit()
        if cursor.rowcount > 0:
            print("## Patient Updated ##")
        else:
            print("## Patient ID not found ##")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except mycon.Error as err:
        print(f"Database Error: {err}")

def display_patients(connection):
    """Display all patient records from the database."""
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM patients"
        cursor.execute(query)
        result = cursor.fetchall()
        print("\n{:<10} {:<20} {:<5} {:<10} {:<30} {:<15}".format("ID", "Name", "Age", "Gender", "Address", "Phone"))
        for row in result:
            print("{:<10} {:<20} {:<5} {:<10} {:<30} {:<15}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
    except mycon.Error as err:
        print(f"Database Error: {err}")

def main():
    """Main function to drive the menu and execute operations."""
    connection = create_connection()
    if connection is None:
        return

    setup_database(connection)

    choice = None
    while choice != 0:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. Delete Patient")
        print("3. Update Patient")
        print("4. Display Patients")
        print("0. Exit")
        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("## Invalid input. Please enter a number. ##")
            continue

        if choice == 1:
            add_patient(connection)
        elif choice == 2:
            delete_patient(connection)
        elif choice == 3:
            update_patient(connection)
        elif choice == 4:
            display_patients(connection)
        elif choice == 0:
            connection.close()
            print("## Bye!! ##")
        else:
            print("## INVALID CHOICE ##")

if __name__ == "__main__":
    main()
