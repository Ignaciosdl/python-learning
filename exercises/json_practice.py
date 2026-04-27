# import json library to work with json files
import json

# list of expenses to save
expenses = [
    {"name":"banana", "category": "food", "amount": 4}, 
    {"name":"fuel", "category": "transport", "amount": 5}
]

# open/create expenses.json in write mode and save expenses list
with open("practice_expenses.json", "w") as file: # "w" = write, creates file if not exists
    json.dump(expenses, file) # convert expenses list to JSON and write to file

# open expenses.json in read mode and load data into expenses variable   
with open("practice_expenses.json", "r") as file: # "r" = read
    expenses = json.load(file) # read JSON from file and convert to Python list

# print loaded data to verify it worked   
print(expenses)