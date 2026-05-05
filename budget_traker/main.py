from budget import set_budget, add_expense, available_budget, category_expenses, budget_alert
from storage import load_data, save_data


budget = set_budget(-100)
print(budget)
expenses = []
add_expense(expenses,"banana","food", 45)
add_expense(expenses,"fuel", "transport", 35)
print(expenses)
print(available_budget(budget, expenses))
print(category_expenses(expenses))
budget_alert(budget,expenses)

# def menu_input():
#     while True:
#         try:
#             option = int(input(f"""
#             === BUDGET TRAKER ===
#             Please enter one of the following numbers:
#             1. Set budget
#             2. Add expenses
#             3. View total expenses
#             4. View availabe budget 
#             5. View expenses by category
#             6. Exit
#             """))
#             if option == 1:
#                 budget =