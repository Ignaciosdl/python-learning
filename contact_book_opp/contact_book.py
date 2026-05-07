# Project 4: Contact Book with OOP
# Refactor the Contact Book project using Object Oriented Programming.
# Create a Contact class with name, phone and email attributes.
# Create a ContactBook class that manages a list of Contact objects with methods:
# add_contact(), search_contact(), view_contacts(), delete_contact()
# and persistence with JSON (load and save).
# Implement an interactive menu in main() to interact with the user.

class Contact: # represents a single contact with its attributes
    def __init__(self, name, phone, email): # initialize contact attributes
        self.name = name 
        self.phone = phone
        self.email = email
    
    def __str__(self): # string representation of a Contact object
        return f"{self.name}, {self.phone}, {self.email}"

class ContactBook: # manages a collection of Contact objects
    def __init__(self): # initialize with empty contacts list
        self.contacts = []
    
    def add_contact(self, name, phone, email): # create and add a new Contact object to the list
        self.contacts.append(Contact(name, phone, email)) # instantiate Contact and append to list


book = ContactBook() # instantiate ContactBook object

book.add_contact("Ignacio", "123", "igna@email.com") # add a contact to the book

for contact in book.contacts:
    print(contact) # print each contact

