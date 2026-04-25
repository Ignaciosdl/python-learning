# list to store all expenses
expenses = [] 

# function to add dictionaries to list
def add_expense(name, category, amount):
    expenses.append({"name":name, "category":category, "amount":amount}) # add dictionary to list

add_expense("bread","food",3) 
add_expense("fuel","transport",20)
add_expense("celphone","telecomunication",10)
print(expenses)

# function to calculate total all the expenses
def total_expenses():
    expenses_amounts = [] # list to store all expenses amounts
    for expense in expenses:
        expenses_amounts.append(expense["amount"]) # add amount to list
    return sum(expenses_amounts) # total sum of all expenses amounts 
    
print(total_expenses())

# function to see all the expenses
def all_expenses():
    for expense in expenses:
        print(f"{expense["name"]}: ${expense["amount"]}") # Shows for each expense it amount

all_expenses()

# expenses grouped by category function
def expenses_category():
    categories_total = {} # Dictionary to store all expenses amounts by category
    for expense in expenses:
        if categories_total.get(expense["category"]) is None: # If the category name doesnt exist in the dictionary
            categories_total[expense["category"]] = expense["amount"] # Create a new category name and asign its amount
        else: #  If the category name exist in the dictionary
            categories_total[expense["category"]] = categories_total[expense["category"]] + expense["amount"] # Sum the new amount to the existing amount of that category
    print(categories_total) # Shows in terminal the total of each category

expenses_category()  
