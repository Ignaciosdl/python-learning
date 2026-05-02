from contacts import contacts, add_contact, search_contact, delete_contact # import the the functions from contacts.py module

add_contact("Ignacio","303456","igna@tuemial.com")
search_contact(contacts,"Ignacio")
search_contact(contacts,"Maria")

print(contacts)
delete_contact(contacts,"Ignacio")
print(contacts) 