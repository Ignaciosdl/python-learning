# creating a dictionary - key: value pairs
person = {
    "name": "Ignacio",
    "age": 34,
    "city": "Byron",
    "is_programmer": True
}

# accessing values by key
print(person["name"]) # -> Ignacio
print(person["age"]) # -> 34
print(person["city"]) # -> Byron

# modifying a dictionary
person["age"] = 35          # modifying an existing key -> "age": 35,
person["job"] = "developer" # adding a new key "job": "developer",
del person["city"]          # deleting a key 

print(person) # After modification -> {'name': 'Ignacio', 'age': 35, 'is_programmer': True, 'job': 'developer'}

# useful dictionary methods
print(person.keys())    # all keys -> dict_keys(['name', 'age', 'is_programmer', 'job'])
print(person.values())  # all values -> dict_values(['Ignacio', 35, True, 'developer'])
print(person.items())   # all key-value pairs -> dict_items([('name', 'Ignacio'), ('age', 35), ('is_programmer', True), ('job', 'developer')])

# looping over a dictionary
for key, value in person.items():
    print(f"{key}: {value}")
    
# list of dictionaries - very common in real world data
people = [
    {"name": "Ignacio", "age": 34, "job": "developer"},
    {"name": "Maria", "age": 25, "job": "designer"},
    {"name": "Juan", "age": 28, "job": "data scientist"}
]

for person in people:
    print(f"{person['name']} is {person['age']} years old and works as {person['job']}")