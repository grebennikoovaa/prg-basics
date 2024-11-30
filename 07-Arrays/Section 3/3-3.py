# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
i = 0
total_food = 0
for row in monthly_expenses:
    total_food += monthly_expenses[i][0]
    i += 1

i = 0 
total_transport = 0
for row in monthly_expenses:
    total_transport += monthly_expenses[i][1]
    i += 1

i = 0
total_utilities = 0
for row in monthly_expenses:
    total_utilities += monthly_expenses[i][2]
    i += 1
        
i = 0 
total_week_1 = 0
for item in monthly_expenses:
    total_week_1 += monthly_expenses[0][i]
    i += 1

i = 0
total_week_2 = 0
for item in monthly_expenses:
    total_week_2 += monthly_expenses[1][i]
    i += 1

i = 0
total_week_3 = 0
for item in monthly_expenses:
    total_week_3 += monthly_expenses[2][i]
    i += 1

i = 0
total_week_4 = 0
for item in monthly_expenses:
    total_week_4 += monthly_expenses[3][i]
    i += 1

total = total_week_1 + total_week_2 + total_week_3 + total_week_4

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',total_food )
print('Transport:', total_transport)
print('Utilities:', total_utilities)
print('Week 1:',total_week_1)
print('Week 2:',total_week_2)
print('Week 3:',total_week_3)
print('Week 4:',total_week_4)
print('---------------')
print('TOTAL:',total)