categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max_expense = max(expenses)
max_index = expenses.index(max_expense)
most_expensive_category = categories[max_index]

print(f"The most expensive expense category was '{most_expensive_category}' with an expense of {max_expense}.")

