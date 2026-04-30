import json # import json library to work with json files
from pathlib import Path # Import path from library pathlib

# load saved contacts at startup
def load_contacts():
    file_path = Path("contacts.json") 
    if file_path.is_file(): 
        with open(file_path, "r") as file:
            contacts = json.load(file)
    else:
        contacts = []
    return contacts

# save contacts at completion
def save_contacts(contacts):
    file_path = Path("contacts.json")
    with open(file_path, "w") as file:
        json.dump(contacts, file)