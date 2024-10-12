price = input('Enter price: ')
starting_price = float(price)
discount = input('Enter discount: ')
percentage_of_discount = float(discount)

price_with_discount = starting_price * (percentage_of_discount/100)
reduction = starting_price - price_with_discount

print(f'Enter price: {starting_price:.2f}')
print(f'Enter discount: {percentage_of_discount:.2f}')
print(f'Price with discount: {price_with_discount:.2f}')
print(f'Reduction: {reduction:.2f}')
