from contacts import contacts, add_contact, search_contact, delete_contact, view_contacts # import the the functions from contacts.py module

add_contact("Ignacio","303456","igna@tuemial.com")
add_contact("Maria","123405","mari@tuemial.com")
add_contact("Pili","876405","pili@tuemial.com")
search_contact(contacts,"Ignacio")
search_contact(contacts,"Quique")

print(contacts)
delete_contact(contacts,"Ignacio")
delete_contact(contacts,"Maria")
delete_contact(contacts,"Pili")
view_contacts(contacts)
 