from storage import load_contacts, save_contacts # import the the functions from storage.py module
from contacts import add_contact, search_contact, delete_contact, view_contacts # import the the functions from contacts.py module

contacts = load_contacts() # calling the function load_contacts and add it to contacts variable

def menu_input(contacts):
    while True: # keep the menu running until the user chooses to exit (option 5)
        try:
            option = int(input("""
            === CONTACTS MANAGER ===
            Please enter one of the following numbers:
            1. Add contact
            2. Search contact
            3. View contacts
            4. Delete contacts
            5. Exit
            """))
            if option == 1:
                name = input(f"Insert the name of the contact to add: ")
                phone = input(f"Insert the phone of the contact to add: ")
                email = input(f"Insert the email of the contact to add: ")
                add_contact(contacts, name, phone, email)
            elif option == 2:
                name = input(f"Please insert the contact name to search: ")
                search_contact(contacts, name)
            elif option == 3:
                view_contacts(contacts)
            elif option == 4:
                name = input(f"Please insert the contact name to be deleted: ")
                delete_contact(contacts, name)
            elif option == 5:
                save_contacts(contacts)
                break
            else:
                print("Please enter a valid number from 1 to 5")
        except ValueError:
                print("Please enter a valid number from 1 to 5")

menu_input(contacts)          
                
                
 