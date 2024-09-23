import csv # to read and write csv file
import os # to check if the file exists
import re # to validate email 

FILE_PATH = 'contacts.csv'

def load_contacts():
    """Load contacts from the CSV file into a dictionary."""
    contacts = {}
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    name, phone, email = row
                    contacts[name] = {'phone': phone, 'email': email}
    return contacts

def save_contacts(contacts):
    """Save contacts from the dictionary to the CSV file."""
    with open(FILE_PATH, 'w', newline='') as file:
        writer = csv.writer(file)
        for name, info in contacts.items():
            writer.writerow([name, info['phone'], info['email']])

def display_menu():
    """Display the menu options to the user."""
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Edit Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. List Contacts")
    print("6. Exit")

def validate_phone(phone):
    """Validate the phone number format."""
    return len(phone) == 11 and phone.isdigit()

def validate_email(email):
    """Validate the email format."""
    return re.match(r"^[a-zA-Z0-9._%+-]+@gmail\.com$", email) is not None

def add_contact(contacts):
    """Add a new contact to the dictionary and save to the file."""
    name = input("Enter contact name: ")
    if name in contacts:
        print(f"Contact '{name}' already exists.")
        return
    phone = input("Enter phone number (11 digits): ")
    if not validate_phone(phone):
        print("Error: Phone number must be 11 digits.")
        return
    email = input("Enter email address (must be @gmail.com): ")
    if not validate_email(email):
        print("Error: Email must be a valid Gmail address.")
        return
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact '{name}' added.")
    save_contacts(contacts)

def edit_contact(contacts):
    """Edit an existing contact's details."""
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        phone = input("Enter new phone number (11 digits): ")
        if not validate_phone(phone):
            print("Error: Phone number must be 11 digits.")
            return
        email = input("Enter new email address (must be @gmail.com): ")
        if not validate_email(email):
            print("Error: Email must be a valid Gmail address.")
            return
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact '{name}' updated.")
        save_contacts(contacts)
    else:
        print("Contact not found.")

def delete_contact(contacts):
    """Delete a contact from the dictionary and the file."""
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
        save_contacts(contacts)
    else:
        print("Contact not found.")

def search_contact(contacts):
    """Search for a contact and display their details."""
    name = input("Enter the name of the contact to search for: ")
    if name in contacts:
        contact = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    else:
        print("Contact not found.")

def list_contacts(contacts):
    """List all contacts."""
    if contacts:
        print("\nContacts List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("No contacts to display.")

def main():
    """Main function to run the contact management system."""
    contacts = load_contacts()
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            edit_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '5':
            list_contacts(contacts)
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()