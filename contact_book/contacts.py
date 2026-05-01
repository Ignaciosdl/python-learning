
from storage import load_contacts, save_contacts # import the the functions from storage.py module

contacts = load_contacts() # Calling the function load_contacts and add it to contacts variable

# function to add dictionaries to list
def add_contact(name,phone,email):
    contacts.append({"name":name, "phone":phone, "email":email}) # Add each contact to contacts list


    