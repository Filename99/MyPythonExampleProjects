import csv

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contact = Contact(name, phone, email)
    contacts.append(contact)

def search_contact():
    query = input("Enter name or phone number: ")
    results = []
    for contact in contacts:
        if query in contact.name or query in contact.phone:
            results.append(contact)
    if results:
        for contact in results:
            print(contact.name, contact.phone, contact.email)
    else:
        print("No contacts found.")

def display_contacts():
    for contact in contacts:
        print(contact.name, contact.phone, contact.email)

def export_csv():
    with open("contacts.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Phone", "Email"])
        for contact in contacts:
            writer.writerow([contact.name, contact.phone, contact.email])
    print("Contacts exported to contacts.csv")

while True:
    print("1. Add contact")
    print("2. Search contact")
    print("3. Display all contacts")
    print("4. Export contacts as CSV")
    print("5. Quit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        display_contacts()
    elif choice == "4":
        export_csv()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Try again.")
