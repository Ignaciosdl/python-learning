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
            found = True # change the value of the variable to describe that the name was found
            break # once the contact was founded by the name we stop the loop
    if found ==False:
        print(f"{name} is not in the list of contact") # if the contact was not found once the loop finished whe show this

# function to delete a dictionaries from a list
def delete_contact(contacts,name):
    found = False # create variable to describe that the name was not found yet
    for contact in contacts: # iterating the list contacts
        if contact["name"] == name: # if the name is in the list
            while True: # the program will be run until the breaks stop it
                    delete = input(f"Are you sure you want to delete this contact Name: {contact["name"]} y/n?")
                    if delete == "y": # if the user want to delete it
                        print(f"The contact: Name: {contact["name"]}, Phone: {contact["phone"]}, Email: {contact["email"]} have been removed")
                        contacts.remove(contact) # delete the dictionary from the contacts list
                        found = True # change the value of the variable to describe that the name was found
                        break # once the contact is removed the program stop
                    elif delete == "n": # if the user dont want to delet it
                        print(f"Deletion cancelled")
                        found = True
                        break
                    else:
                        print("Please enter y or n")
    if found == False: # if the contact is not founded after the complete iteration
        print(f"{name} is not in the list of contact") # if the contact was not found once the loop finished whe show this
        