# list to store all expenses
expenses = [] 

# function to add dictionaries to list
def add_expense(name, category, amount):
    expenses.append({"name":name, "category":category, "amount":amount}) # add dictionary to list

add_expense("bread","food",3) 
add_expense("fuel","trasport",20)
add_expense("celphone","telecomunicaction",10)
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
        print(f"{expense["name"]}: ${expense["amount"]}")

all_expenses()

