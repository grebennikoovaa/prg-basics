# File name
file_name = 'it_company.csv'

# Position to filter
job_title = 'Software Engineer'

# Open the file and process its content
with open(file_name, 'r') as file:
    # Enumerate over the lines in the file
    count = 1  # Start numbering from 1
    for line in file:
        if job_title in line:
            print(f"{count}. {line.strip()}")
            count += 1