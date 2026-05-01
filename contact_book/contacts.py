
from storage import load_contacts, save_contacts # import the the functions from storage.py module

contacts = load_contacts() # calling the function load_contacts and add it to contacts variable

# function to add dictionaries to list
def add_contact(name,phone,email):
    contacts.append({"name":name, "phone":phone, "email":email}) # add each contact to contacts list

# function to search contact by name
def search_contact(contacts, name):
    found = False # create variable to describe that the name was not found yet
    for contact in contacts: # iterating the list contacts
        if contact["name"] == name: # if the name is in the list shows:
            print(f"Name: {contact["name"]}, Phone: {contact["phone"]}, Email: {contact["email"]}") 
            found = True # change the value of the variable to describe that the name was founde
            break # once the contact was founded by the name we stop the loop
    if found ==False:
        print(f"{name} is not in the list of contact") # if the contact was not found once the loop finished whe show this
    