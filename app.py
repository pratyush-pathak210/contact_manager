from database import create_table
import sqlite3

create_table()

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
        (name, phone, email)
    )

    conn.commit()
    conn.close()
    print("Contact added successfully!")

def view_contacts():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()

    for contact in contacts:
        print(contact)

    conn.close()

def main():
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
