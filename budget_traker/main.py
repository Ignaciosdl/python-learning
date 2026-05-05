from budget import set_budget, add_expense, available_budget, category_expenses, budget_alert, get_total_expenses # import all functions from budget module
from storage import load_data, save_data # import load and save functions from storage module

# function to prompt user to set a budget amount with validation
def budget_input():
    while True: # keep asking until a valid amount is entered
        try:
            amount = int(input("Please set a monthly budget amount: ")) # ask user for budget amount and convert to int
            budget = set_budget(amount) # validate and set the budget
            break # exit loop if valid
        except ValueError: 
            print("Please enter a positive number") # show error if input is invalid
    return budget # return the validated budget amount

# function to display interactive menu and handle user options
def menu_input(budget, expenses): # receives budget and expenses as parameters
        while True: # keep menu running until user exits
            try:
                option = int(input("""
                === BUDGET TRACKER ===
                Please enter one of the following numbers:
                1. Set budget
                2. Add expense
                3. View total expenses
                4. View available budget 
                5. View expenses by category
                6. Exit
                """)) # display menu and get user option
                if option == 1:
                   budget = budget_input() # prompt user to set a new budget
                   budget_alert(budget, expenses) # check if budget alert should be shown
                elif option == 2:
                    name = input("Insert the name of the expense to add:") # get expense name
                    category = input("Insert the category of the expense:") # get expense category
                    while True: # keep asking until valid amount is entered
                        try:
                            amount = int(input("Insert the amount of the expense:")) # get expense amount
                            break # exit loop if valid
                        except ValueError:
                            print("Please enter a valid number") # show error if input is invalid
                    add_expense(expenses, name, category, amount) # add expense to the list
                    budget_alert(budget, expenses) # check if budget alert should be shown
                elif option == 3:
                    print(f"Total of expenses: {get_total_expenses(expenses)}") # show total expenses
                    budget_alert(budget, expenses) # check if budget alert should be shown
                elif option == 4:
                    print(f"Budget available: {available_budget(budget, expenses)}") # show available budget
                    budget_alert(budget, expenses) # check if budget alert should be shown
                elif option == 5:
                    print(category_expenses(expenses)) # show expenses grouped by category
                    budget_alert(budget, expenses) # check if budget alert should be shown
                elif option == 6:
                    save_data(budget, expenses) # save all data to json file before exiting
                    break # exit the menu loop
                else:
                    print("Please enter a valid number from 1 to 6") # show error for invalid option
            except ValueError:
                    print("Please enter a valid number from 1 to 6") # show error if input is not a number

budget, expenses = load_data() # load saved budget and expenses from json file at startup

if budget == 0: # if no budget has been set yet
    budget = budget_input() # prompt user to set initial budget
    
menu_input(budget, expenses) # start the interactive menu
                           