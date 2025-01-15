employees = [("Smith", "Lucy"), ("Jones", "Janet"), ("Lee", "Jerry"),
             ("Jackson", "Peter"), ("Johnson", "Rick"),
             ("Lewis", "Terry"), ("Clarke", "Robin")]

formatted_employees = [f"{last.upper()}, {first}" for last, first in employees]

for employee in formatted_employees:
    print(employee)