import csv

def read_file():
    books = []
    with open('books.csv', 'r') as file:
         content = csv.reader(file)
         next(content)
         for row in content:
              books.append(row)
    return books

