import json # import json library to work with json files
from pathlib import Path # import path from library pathlib

# load saved data at startup
def load_data():
    file_path = Path("data.json") # create an object (file_path) that represent the path of the file data.json
    if file_path.is_file(): # in this path exist a file? If yes then:
        with open(file_path, "r") as file: # open the file in read mode
            data = json.load(file) # load the information from json in dictionary format and store it in the variable data 
            budget = data["budget"] # accessing to dictionary values by key 
            expenses = data["expenses"] # accessing to dictionary values by key 
    else: # if there isnt a file on this path then:
        budget = 0 # creates a variable budget with int value starting on zero
        expenses = [] # creates the variable expenses as an empty list
    return budget, expenses

# serialize budget amount and expenses list and save to json file
def save_data(budget,expenses): # the function receives two parameters
    file_path = Path("data.json") # create an object (file_path) that represent the path of the file data.json
    data = {"budget":budget, "expenses":expenses} # create a variable data that is a dictionary containing budget and expenses
    with open(file_path, "w") as file: # open the json file in write mode
        json.dump(data, file) # save all the changes from python on a json format file
