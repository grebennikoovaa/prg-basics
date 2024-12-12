import csv

with open('it_company.csv', 'r') as file:
    reader = csv.DictReader(file)  
    for row in reader:
        if row['Job Title'] == 'Graphic Designer':
            first_name = row['First Name']
            last_name = row['Last Name']
            email = row['Email']
            print(f"{first_name} {last_name},{email}")