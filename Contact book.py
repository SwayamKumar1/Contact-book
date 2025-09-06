import json

try:
    with open('contacts.json', "r") as file:
        contact = json.load(file)
except FileNotFoundError:
    contact = {}

def save_contacts():
    with open('contacts.json', "w") as file:
        json.dump(contact, file, indent=4)

def add_contact(name, phone):
    contact[name.lower()] = {"name": name, "phone": phone}
    save_contacts()

def search_contact(name):
    return contact.get(name.lower(), "contact not found")

def update_contact(name, phone):
    if name.lower() in contact:
        contact[name.lower()]["phone"] = phone
        save_contacts()
    else:
        return "contact not found"
    
def show_all_contacts():
    return contact

def delete_contact(name):
    if name.lower() in contact: 
        del contact[name.lower()]
        save_contacts()
    else:
        return "contact not found"

while True:
    print("Contact Book Menu: ")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Show all Contacts")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        add_contact(name, phone)
        print("Contact added successfully!")

    elif choice == '2':
        name = input("Enter contact name to search: ")
        result = search_contact(name)
        if isinstance(result, dict):   
            print("Phone number:", result["phone"])
        else:
            print(result)

    elif choice == '3':
        name = input("Enter contact name to update: ")
        phone = input("Enter new phone number: ")
        result = update_contact(name, phone)
        if result:
            print(result)
        else:
            print("Contact updated successfully!")

    elif choice == '4':
        contacts = show_all_contacts()
        if contacts:
            for key, info in contacts.items():
                print("Name:", info["name"], "Phone:", info["phone"])
        else:
            print("No contacts found.")

    elif choice == '5':
        name = input("Enter contact name to delete: ")
        result = delete_contact(name)
        if result:
            print(result)
        else:
            print("Contact deleted successfully!")

    elif choice == '6':
        print("Goodbye!")
        break

