contacts = []

def add_contact():
    Name = input("Enter contact name: ")
    Phone = input("Enter phone number: ")
    Email = input("Enter email address: ")
    contacts.append({"name": Name, "phone": Phone, "email": Email})
    print("Contact added successfully! ")

def view_contact():
    if not contacts:
        print("No contacts found!")
        return
    else:
        for i, contact in enumerate (contacts, 1):
            print(f"{i}. Name: {contact["name"]}, Phone number: {contact["phone"]}, Email: {contact["email"]}")

def search_contact():
    search_name = input("Enter contact name to search: ")
    found = False
    for contact in contacts:
        if search_name.lower() == contact["name"].lower():
            print("Contact found! ")
            print(f"Name: {contact["name"]}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            found = True
            break
    if not found:
        print("Contact not found! ")

def update_contact():
    update_name = input("Enter contact name to update: ")
    found = False
    for contact in contacts:
        if update_name.lower() == contact["name"].lower(): 
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email address: ")
            contact["phone"] = new_phone
            contact["email"] = new_email
            print("Contact updated successfully! ")
            found = True
            break
    if not found:
        print("Contact not found! ")

def delete_contact():
    delete_name = input("Enter contact name to delete: ")
    found = False
    for contact in contacts:
        if delete_name.lower() == contact["name"].lower():
            contacts.remove(contact)
            print("Contact deleted successfully! ")
            found = True
            break
    if not found:
        print("Contact not found! ")
        
while True:
    print("WELCOME TO CONTACT BOOK")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter what task you want to perform (1/2/3/4/5/6): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contact()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank you for using Contact Book! ")
        break

    else:
        print("Invalid choice! Please select from 1 to 6")