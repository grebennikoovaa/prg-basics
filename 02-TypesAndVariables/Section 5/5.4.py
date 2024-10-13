amount_string = input('Enter the amount: ')
amount = float(amount_string)
vat = amount * 0.23
total_amount = vat + amount
print(f'Amount:', total_amount)
print(f'Vat 23%:', vat)