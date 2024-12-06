price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

for key, value in price_list.items():
    print(key, value)

sum_before_discount = sum(price_list.values())
print(sum_before_discount)

discount_list = {}
for key, value in price_list.items():
    discount = round((90*value)/100, 2)
    discount_list[key] = discount
print(f"\nProducts and their prices after the 10% discount: {discount_list}")

total_discount_list = sum(discount_list.values())
print(total_discount_list)