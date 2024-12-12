import csv

with open('clothing.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        price = int(row['Price'])
        stock_quantity = int(row['Stock_Quantity'])
        if price < 60:
            if stock_quantity < 40:
                product_name = row['Product_Name']
                category = row['Category']
                size = row['Size']
                color = row['Color']
                print(f'{product_name}, {category}, {size}, {color}, {price}, {stock_quantity}')
