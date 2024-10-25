###
# Program that calculates the amount to be paid
#

num_of_products = int(input('Enter the number of products purchased: '))
product_price = float(input('Enter the product price: '))

if num_of_products >= 2:
     discount_price = product_price * 0.75  # 25% discount 
     total_amount = (product_price * 2) + ((num_of_products - 2) * discount_price)
else:
    total_amount = num_of_products * product_price
print(f"Amount to pay: {total_amount}")