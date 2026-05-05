from budget import set_budget, add_expense, available_budget, category_expenses, budget_alert

budget = 0
budget = set_budget(budget, 100)
print(budget)
expenses = []
add_expense(expenses,"banana","food",45)
add_expense(expenses,"fuel","transport",35)
print(expenses)
print(available_budget(budget,expenses))
print(category_expenses(expenses))
budget_alert(budget,expenses)