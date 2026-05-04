# function to modify the budget amount
def set_budget(budget,amount): # function receives two parameters budget and amount
    budget = amount # asign the amount as a parameter to the variable budget
    return budget # return budget with the new amount value

# function to add dictionaries with name, category and amout to the expenses list
def add_expense(expenses, name, category, amount): 
    expenses.append({"name":name, "category":category, "amount":amount}) # adding dcitionaries to list with append method