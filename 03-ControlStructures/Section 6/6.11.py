###
# Program that analyses the price of a product in an online store
#

current_product_price = float(input('Enter current product price: '))
previous_product_price = float(input('Enter previous product price: '))

price_decrease = (previous_product_price - current_product_price / previous_product_price) * 100

if price_decrease >= 10:
    print("Buy the product!")
    print(f"Product price reduced by {price_decrease}%")
else:
    print("Do not buy the product")