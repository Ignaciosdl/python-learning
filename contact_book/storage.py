import json # import json library to work with json files
from pathlib import Path # import path from library pathlib

# load saved contacts at startup
def load_contacts():
    file_path = Path("contacts.json") # create the path to the file contact.json
    if file_path.is_file(): # does this path has a file?
        with open(file_path, "r") as file: # if exists then open it in read mode
            contacts = json.load(file) # load the information and store it in the variable contacts
    else:
        contacts = [] # If the file doesnt exist then create the variable contact as an empty list
    return contacts

# serialize contacts list and save to json file
def save_contacts(contacts): 
    file_path = Path("contacts.json") # look for the file path
    with open(file_path, "w") as file: # open it in write mode
        json.dump(contacts, file) # save all the changes on a json file
        
