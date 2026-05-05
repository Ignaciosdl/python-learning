# function to modify the budget amount
def set_budget(budget,amount): # function receives two parameters budget and amount
    budget = amount # asign the amount as a parameter to the variable budget
    return budget # return budget with the new amount value

# function to add dictionaries with name, category and amout to the expenses list
def add_expense(expenses, name, category, amount): 
    expenses.append({"name":name, "category":category, "amount":amount}) # adding dcitionaries to list with append method

# function to calculate the total amount of expenses    
def get_total_expenses(expenses): # receives the expenses list a parameter
    total_expenses =  sum(map(lambda expense: expense["amount"], expenses)) # extract amount from each expense and calculate total with map() and sum()
    return total_expenses # return the total amount of expenses

# function to calculate the availabel budget    
def available_budget(budget,expenses): # receives two parameters budget and expenses
    total_expenses =  get_total_expenses(expenses) # call the function get_total_expenses to calculate the total amount of expenses
    available_budget = budget - total_expenses # rest the total of expenses from the mensual budget
    return available_budget # return the available budget

# function to calculate the total amount of expenses by category
def category_expenses(expenses):
    categories_total = {} # create an empty dictionary to store all categories with their amounts
    for expense in expenses: # iterate the list of expenses
        if categories_total.get(expense["category"]) == None: # if the category that we are looking for is not part of the categories_total dictionarie then:
            categories_total[expense["category"]] = expense["amount"] # we create a new key with it value
        else: # if the category that we are looking for is part of the categories_total dictionarie then:
            categories_total[expense["category"]] = categories_total[expense["category"]] + expense["category"] # we add the amount to the value of the existing key
    return categories_total

