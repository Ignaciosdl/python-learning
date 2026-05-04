from budget import set_budget, add_expense, available_budget

budget = 0
budget = set_budget(budget, 1000)
print(budget)
expenses = []
add_expense(expenses,"banana","food",5)
add_expense(expenses,"fuel","transport",15)
print(expenses)
print(available_budget(budget,expenses))
