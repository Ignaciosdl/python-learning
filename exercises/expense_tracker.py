# list to store all expenses
expenses = [] 

# function to add dictionaries to list
def add_expense(name, category, amount):
    expenses.append({"name":name, "category":category, "amount":amount}) # add dictionary to list

add_expense("bread","food",3) 
add_expense("fuel","trasport",20)
add_expense("celfone","telecomunicactions",10)
print(expenses)

# function to calculate all the expenses
def total_expenses():
    expenses_amounts = [] # list to store all expenses amounts
    for expense in expenses:
        expenses_amounts.append(expense["amount"]) # add amount to list
    return sum(expenses_amounts) # total sum of all expenses amounts 
    
print(total_expenses())

